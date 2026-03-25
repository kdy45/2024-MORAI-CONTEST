#!/usr/bin/env python3

import rospy
import roslib
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int32MultiArray
from cv_bridge import CvBridge
from morai_msgs.msg import CtrlCmd
from math import *
import numpy as np
import cv2
from time import *


class camReg :
    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node("open_camera")

        rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.img_CB)
        
        self.moment_point = rospy.Publisher("/moment_pts", Int32MultiArray, queue_size=3)

        self.ctrl_cmd_msg = CtrlCmd()

        # =======================
        self.imgWidth = 1280              # image Width
        self.imgHeight = 720              # image Height

        # crop image for line detection
        self.cropOffsetWidth = 200        # offset X from left/right line for crop image
        self.cropOffsetHeight = 0         # offset Y from bottom line for crop image

        # Size of crop Image
        self.cropImageWidth = 840
        self.cropImageHeight = 250
        self.cropImageHalfWidth = 420
        # ====================================

        self.imgHalfWidth = self.imgWidth // 2   # image Half Width

        self.setCropImgWidth(offsetWidth=0, cropWidth=840)
        self.setCropImgHeight(offsetHeight=0, cropHeight=250)

        # Driving point of left line
        self.lx = 0
        self.ly = 0

        # Driving point of right line
        self.rx = 0
        self.ry = 0

        # For img_canny
        # 15번의 좌우측 이동 좌표를 저장하고 새로운 좌표와 평균을 구하여 이동할 좌표를 구한다.  
        self.prev_r_mv = MovingAverage(15)
        self.prev_l_mv = MovingAverage(15)
        self.prev_flag = False
        self.line_find = ""

        self.image_ON = False

        self.start_time = rospy.get_time()

    def setCropImgWidth(self, offsetWidth=0, cropWidth=400) :
        self.cropOffsetWidth = offsetWidth
        self.cropImageWidth = cropWidth
        self.cropImageHalfWidth = cropWidth // 2

        self.crop_lx_left = self.cropOffsetWidth
        self.crop_rx_left = self.crop_lx_left + cropWidth

        self.crop_rx_right = self.imgWidth - self.cropOffsetWidth
        self.crop_lx_right = self.crop_rx_right - cropWidth

    def setCropImgHeight(self, offsetHeight=100, cropHeight=100) :
        self.cropOffsetHeight = offsetHeight
        self.cropImageHeight = cropHeight

        self.crop_upper_y = self.imgHeight - self.cropOffsetHeight
        self.crop_lower_y = self.crop_upper_y - self.cropImageHeight

    # self.rx : 우측차선이 중앙으로부터 떨어진 거리
    # self.lx : 좌측 차선이 좌측 이미지로부터 떨어진 거리 (중앙으로부터 떨어진 거리 = 320 - lx)
    def pub_commands(self) :
        self.end_time = rospy.get_time()

        moment_pts = Int32MultiArray()
        moment_pts.data = [self.cropImageWidth, self.cropImageHeight, self.lx, self.ly, self.rx, self.ry]

        # 10Hz Publish
        if self.end_time - self.start_time >= 0.1:
            self.start_time = self.end_time
            self.moment_point.publish(moment_pts)
    
    def img_canny(self, img) :
        img_crop = img.copy()[self.crop_lower_y:self.crop_upper_y, self.crop_lx_left:self.crop_rx_right]

        img_gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (27, 27), 0)
        img_edge = cv2.Canny(np.uint8(img_blur), 100, 123)
        edges = cv2.HoughLinesP(img_edge, 1, np.pi/180, 15, 15, 1)

        slopes = []
        lines = []
        seta = []

        # 모든 edge에 대한 기울기를 구해 각도가 너무 작은 것은 제외하고 저장(slopes, lines, seta)
        if type(edges) == type(None):  
            pass
        else:
            for edge in edges:            
                x1, y1, x2, y2 = edge[0]
                if (x2-x1) == 0:
                    slope = 0
                    deg = 0
                else:
                    slope = float(y2-y1)/float(x2-x1)
                    rad = atan(slope) 
                    deg = rad * 180/pi 
                            
                # 각도가 너무 작은 것은 차선이 아니다.
                if 22 <= abs(deg) :   
                    slopes.append(slope)
                    lines.append(edge[0])               
                    seta.append(deg)                    

        # 좌우 차선에 대한 line을 분리한다.
        left_lines = []
        right_lines = []

        for idx, line in enumerate(lines) :
            slope = slopes[idx]
            x1,y1, x2,y2 = line
           
            if (slope < 0) and (x2 < self.cropImageHalfWidth):   
                left_lines.append([line.tolist()])

            if (slope > 0 ) and (x1 > self.cropImageHalfWidth):  
                right_lines.append([line.tolist()])                    

        if (self.image_ON) :
            # Draw Left Lines on img
            for line in left_lines:  
                if all(line[0]):  
                    x1,y1, x2,y2 = line[0]            
                    cv2.line(img,(x1 + self.cropOffsetWidth, y1 + self.crop_lower_y),
                            (x2 + self.cropOffsetWidth, y2 + self.crop_lower_y),(255,0,0),3) 

            # Draw Right Lines on img
            for line in right_lines: 
                if all(line[0]):
                    x1,y1, x2,y2 = line[0]
                    cv2.line(img,(x1 + self.cropOffsetWidth, y1 + self.crop_lower_y),
                            (x2 + self.cropOffsetWidth, y2 + self.crop_lower_y),(0,0,255),3) 

        # 검출된 왼쪽 차선에 대하여 대표(중간) 차선을 계산하여 만든다.
        # 차선(y=mx + b)에 대한 기울기(m)와  y좌표 상수(b)를 구한다.
        x_sum, y_sum, m_sum = 0.0, 0.0, 0.0
        x_avg, y_avg = 0, 0
        m_left, b_left = 0.0, 0.0
        size = len(left_lines)

        for line in left_lines:
            x1,y1, x2,y2 = line[0]
            x_sum += x1 + x2
            y_sum += y1 + y2
            m_sum += float(y2 - y1) / float(x2 - x1)
        
        if size == 0:
            x1 = 0
            x2 = 0          
            cv2.line(img,(x1,0 + self.crop_lower_y),(x2, 720),(0,255,0),2)  
        else : 
            x_avg = x_sum / (size * 2)
            y_avg = y_sum / (size * 2)
            m_left = m_sum / size
            b_left = y_avg - m_left * x_avg
            x1 = int((0.0 - b_left)/ m_left)
            x2 = int((720 - self.crop_lower_y-b_left)/m_left)  
            cv2.line(img, (x1 + self.cropOffsetWidth,0 + self.crop_lower_y),
                     (x2 + self.cropOffsetWidth, 720),(0,255,0),2)

        # 검출된 우측 차선에 대하여 대표(중간) 차선을 계산하여 만든다.
        # 차선(y=mx + b)에 대한 기울기(m)와  y좌표 상수(b)를 구한다.
        x_sum, y_sum, m_sum = 0.0, 0.0, 0.0
        m_right, b_right = 0.0, 0.0
        x_avg, y_avg = 0, 0
        size = len(right_lines)

        for line in right_lines:
            x1,y1, x2,y2 = line[0]
            x_sum += x1 + x2
            y_sum += y1 + y2
            m_sum += float(y2 - y1) / float(x2 - x1)

        if size == 0: 
            m_right = 0        
            b_right = 1280
            x1 = 1280
            x2 = 1280
            cv2.line(img,(x1,0+self.crop_lower_y),(x2,720),(0,255,255),2)
        else:
            x_avg  = x_sum / (size * 2)
            y_avg  = y_sum / (size * 2)
            m_right = m_sum / size
            b_right = y_avg-m_right * x_avg
        
            x1 = int((0.0 - b_right)/ m_right)
            x2 = int((720 - self.crop_lower_y - b_right)/m_right)

            cv2.line(img,(x1 + self.cropOffsetWidth, self.crop_lower_y),
                     (x2 + self.cropOffsetWidth, 720),(0,255,255),2)

        # 차량을 제어하기 위한 Point 찾기 =================
        # 제어를 위한 Point 이력 초기화
        if self.prev_flag == False:
            self.prev_l_mv.add_sample(0)
            self.prev_r_mv.add_sample(0)
            self.prev_flag =True

        # 제어를 위한 기준 Y좌표 설정
        y_height = 140.0  

        # 차선이 검출되지 않은 경우, 15개의 이전 좌표를 사용
        if m_left == 0.0:
            x_left = self.prev_l_mv.get_mm()
        else:
            x_left = int ((y_height-b_left)/m_left)  
        
        if m_right == 0.0:
            x_right = self.prev_r_mv.get_mm()
        else:
            x_right = int((y_height - b_right)/m_right)
        
        # 차선이 검출되지 않은 경우를 위하여 현재 차선 주행 포인트를 저장
        self.prev_l_mv.add_sample(x_left)
        self.prev_r_mv.add_sample(x_right)

        # print(f'self.prev_l_mv.data={self.prev_l_mv.data}, self.prev_l_mv.weights={self.prev_l_mv.weights}')
        # print(f'x_left={x_left}, x_right={x_right}, m_left={m_left}')

        # 차량의 중심선을 이미지에 그리기(디버깅 용)
        if (self.image_ON) :
            y_fix = int(self.crop_lower_y + y_height)
            cv2.line(img,(0, y_fix),(1280, y_fix),(255,55,255),2)     
            cv2.rectangle(img,(640-5, y_fix - 5),(640 + 5, y_fix + 5),(0,0,255),4) 

        # 좌측 차선의 x 좌표 계산
        if m_left == 0.0:
            x_left = 0
        else:
            x_left = int(x_left + self.cropOffsetWidth)
            if x_left < 0 :
                x_left = 0

        # 우측 차선의 x 좌표 계산
        if m_right == 0.0: 
            x_right = self.imgWidth
        else:
            x_right = int(x_right + self.cropOffsetWidth)
            if x_right > self.imgWidth :
                x_right = self.imgWidth
        
        # 제어기로 보낼 Topic을 위하여 저장
        self.lx = x_left
        self.rx = x_right

        # X촤표의 중심을 계산
        if self.line_find == "l":
            x_center = x_left + 340
            # self.CamData.line_find = "l"
        elif self.line_find == "r1":
            x_center = x_right  - 240
            # self.CamData.line_find = "r1"
        elif self.line_find == "r2":
            x_center = x_right - 280
            # self.CamData.line_find = "r2"
        else:
            x_center = (x_left + x_right) // 2
            # self.CamData.line_find = "a"
        
        #print(x_center)
        print(f'lx={x_left}, cx={x_center}, rx={x_right}, y={y_fix}')
        
        cv2.rectangle(img,(x_left - 5, y_fix - 5),(x_left + 5,y_fix + 5),(0,255,255),4)     
        cv2.rectangle(img,(x_right - 5, y_fix - 5),(x_right + 5,y_fix + 5),(255,255,0),4)   
        cv2.rectangle(img,(x_center - 5, y_fix - 5),(x_center + 5,y_fix + 5),(255,0,0),4)   

        # self.CamData.CamAngle = (x_center-roi_x)/((1280-roi_x*2)) 

        # self.pub_commands()   

        # ====================================
        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img", img)

        cv2.namedWindow("img_crop", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img_crop", img_crop)

        cv2.namedWindow("img_gray", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img_gray", img_gray)

        cv2.namedWindow("img_blur", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img_blur", img_blur)
        
        cv2.namedWindow("img_edge", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img_edge", img_edge)
        
        cv2.waitKey(1)
        # ====================================

    def img_CB(self, data):
        img = self.bridge.compressed_imgmsg_to_cv2(data)
        self.img_canny(img)

class MovingAverage (): 

    def __init__(self,n):
        self.samples = n
        self.data = []
        self.weights = list (range(1, n + 1))
    
    def add_sample(self, new_sample):
        if len(self.data) < self.samples:
            self.data.append(new_sample)
        else:
            self.data = self.data[1:] + [new_sample]
    
    def get_mm(self):
        return float(sum(self.data))/len(self.data)
    
    def get_wmm(self):
        s = 0
        for i, x in enumerate(self.data):
            s += x* self.weights[i]
        
        return float(s) / sum(self.weights[:len(self.data)])
    
if __name__ == '__main__' :
    try :
        camReg()
        rospy.spin()
    except rospy.ROSInterruptException :
        pass
