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
        self.imgWidth = 1280                     # image Width
        self.imgHeight = 720                     # image Height

        # crop image for line detection
        self.cropOffsetWidth = 0            # offset X from left/right line for crop image
        self.cropOffsetHeight = 100         # offset Y from bottom line for crop image

        # Size of crop Image
        self.cropImageWidth = 640
        self.cropImageHeight = 200
        # ====================================

        self.imgHalfWidth = self.imgWidth // 2   # image Half Width

        self.setCropImgWidth(offsetWidth=0, cropWidth=640)
        self.setCropImgHeight(offsetHeight=0, cropHeight=200)

        # Define range of white color in HSV
        self.white_lower = np.array([0,0,200])
        self.white_upper = np.array([179,64,255])

        # Define range of yellow color in HSV
        self.yellow_lower = np.array([15, 80, 0])
        self.yellow_upper = np.array([45,255,255])

        # Moment point of left line
        self.lx = 0
        self.ly = 0
        self.lflag = True
        self.lcount = 0

        # Moment point of right line
        self.rx = 0
        self.ry = 0
        self.rflag = True
        self.rcount = 0

        # For img_moment2()
        self.thresh_value = 170

        self.start_time = rospy.get_time()

    def setCropImgWidth(self, offsetWidth=0, cropWidth=400) :
        self.cropOffsetWidth = offsetWidth
        self.cropImageWidth = cropWidth

        self.crop_lx_left = self.cropOffsetWidth
        self.crop_rx_left = self.crop_lx_left + cropWidth

        self.crop_rx_right = self.imgWidth - self.cropOffsetWidth
        self.crop_lx_right = self.crop_rx_right - cropWidth

    def setCropImgHeight(self, offsetHeight=100, cropHeight=100) :
        self.cropOffsetHeight = offsetHeight
        self.cropImageHeight = cropHeight

        self.crop_upper_y = self.imgHeight - self.cropOffsetHeight
        self.crop_lower_y = self.crop_upper_y - self.cropImageHeight

    def detect_color(self, img) :
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only yellow colors
        yellow_mask = cv2.inRange(hsv, self.yellow_lower, self.yellow_upper)

        # Threshold the HSV image to get only white colors
        white_mask = cv2.inRange(hsv, self.white_lower, self.white_upper)

        # Threshold the HSV image to get blend colors
        blend_mask = cv2.bitwise_or(yellow_mask, white_mask)
        blend_color = cv2.bitwise_and(hsv, hsv, mask=blend_mask)

        return blend_color
    
    def binary_image(self, blend_color) :
        bin = cv2.cvtColor(blend_color, cv2.COLOR_BGR2GRAY)
        binary_line = np.zeros_like(bin)
        binary_line[bin != 0] = 1

        return binary_line

    def calculateMoment(self, img):
        x = 0
        y = 0
        dlflag = False
        count = 0

        ML = cv2.moments(img)
        if ( ML['m00'] > 0 ) :
            x = int(ML['m10']/ML['m00'])
            y = int(ML['m01']/ML['m00'])
            dlflag = True

            # Moment 주위의 6x6 내에 Line을 표시하는 점이 몇개 있는지 센다.
            # If noise is existed, Moment is not on the line.  
            # for j in range(3) :
            #     if (x + j >= self.cropImageSizeX) or (x - j < 0) :
            #         continue

            #     for m in range(3) :
            #         if ( y + m >= self.cropImageSizeY ) or (y - m < 0) :
            #             continue

            #         if (img[y + m, x + j] == 1) :
            #             count += 1

            #         if (img[y - m, x - j] == 1) :
            #             count += 1

        return x, y, dlflag, count
    
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

    def img_momentHT(self, data) :
        img = self.bridge.compressed_imgmsg_to_cv2(data)
        crop_img = img.copy()[self.crop_lower_y:self.crop_upper_y, :]

        # create a zero array
        stencil = np.zeros_like(crop_img[:,:,0])

        # specify coordinates of the polygon
        # polygon = np.array([[0,200], [0,0], [1280,0], [1280,200]])
        polygon = np.array([[0,self.cropImageHeight], [300,0], 
                            [self.imgWidth-300,0], [self.imgWidth,self.cropImageHeight]])

        # fill polygon with ones
        cv2.fillConvexPoly(stencil, polygon, 1)

        polygon_img = cv2.bitwise_and(crop_img[:,:,0], crop_img[:,:,0], mask=stencil)

        # Get threshhold image
        ret, thresh_img = cv2.threshold(polygon_img, self.thresh_value, 255, cv2.THRESH_BINARY)

        # Get Hough transform
        lines = cv2.HoughLinesP(thresh_img, 1, np.pi/180, 30, maxLineGap=200)

        line_only_image = np.zeros_like(crop_img[:,:,0])

        # draw Hough lines
        if lines is not None :
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(line_only_image, (x1, y1), (x2, y2), (255, 0, 0), 3)

        left_line = line_only_image.copy()[:, 0:self.cropImageWidth]
        right_line = line_only_image.copy()[:, self.cropImageWidth:self.imgWidth]

        self.lx, self.ly, self.lflag, self.lcount = self.calculateMoment(left_line)
        self.rx, self.ry, self.rflag, self.rcount = self.calculateMoment(right_line)
        if self.rx == 0 :
            self.rx = self.cropImageWidth

        print(f'shape={left_line.shape}, lx={self.lx}, ly={self.ly}, lflag={self.lflag}, lcount={self.lcount}')
        print(f'shape={right_line.shape}, rx={self.rx}, ry={self.ry}, rflag={self.rflag}, rcount={self.rcount}')

        cv2.circle(left_line, (self.lx, self.ly), 3, (0, 255, 0), -1)
        cv2.circle(right_line, (self.rx, self.ry), 3, (0, 255, 0), -1)

        cv2.circle(crop_img, (self.lx, self.ly), 3, (0, 255, 0), -1)
        cv2.circle(crop_img, (self.rx+640, self.ry), 3, (0, 255, 0), -1)

        self.pub_commands()   

        # ====================================
        # cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("img", img)

        cv2.namedWindow("crop_img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("crop_img", crop_img)
                
        cv2.namedWindow("poly_gone_image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("poly_gone_image", polygon_img)

        cv2.namedWindow("Image Threshholding", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Image Threshholding", thresh_img)

        cv2.namedWindow("line_only_image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("line_only_image", line_only_image)

        cv2.namedWindow("left_line", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("left_line", left_line)

        cv2.namedWindow("right_line", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("right_line", right_line)
        
        cv2.waitKey(1)
        # ====================================

    def img_momentHT2(self, data) :
        img = self.bridge.compressed_imgmsg_to_cv2(data)

        crop_img = img.copy()[520:720, :]

        # create a zero array
        stencil = np.zeros_like(crop_img[:,:,0])

        # specify coordinates of the polygon
        # polygon = np.array([[0,470], [140,360], [500,360], [640,470]])
        # polygon = np.array([[0,720], [0,420], [1280,420], [1280,720]])
        polygon = np.array([[0,200], [0,0], [1280,0], [1280,200]])

        # fill polygon with ones
        cv2.fillConvexPoly(stencil, polygon, 1)

        polygone_img = cv2.bitwise_and(crop_img[:,:,0], crop_img[:,:,0], mask=stencil)

        # Get threshhold image
        ret, thresh_img = cv2.threshold(polygone_img, self.thresh_value, 255, cv2.THRESH_BINARY)

        # Get Hough transform
        lines = cv2.HoughLinesP(thresh_img, 1, np.pi/180, 30, maxLineGap=200)

        # create a copy of the original frame
        # dmy = cv_image[:,:,0].copy()

        line_only_image = np.zeros_like(crop_img[:,:,0])

        # draw Hough lines
        if lines is not None :
            for line in lines:
                x1, y1, x2, y2 = line[0]
                # cv2.line(dmy, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.line(line_only_image, (x1, y1), (x2, y2), (255, 0, 0), 3)

        left_binary = line_only_image.copy()[:, 0:640]
        right_binary = line_only_image.copy()[:, 640:1280]

        self.lx, self.ly, self.lflag, self.lcount = self.calculateMoment(left_binary)
        self.rx, self.ry, self.rflag, self.rcount = self.calculateMoment(right_binary)
        if self.rx == 0 :
            self.rx = self.cropImageWidth

        print(f'shape={left_binary.shape}, lx={self.lx}, ly={self.ly}, lflag={self.lflag}, lcount={self.lcount}')
        print(f'shape={right_binary.shape}, rx={self.rx}, ry={self.ry}, rflag={self.rflag}, rcount={self.rcount}')

        cv2.circle(left_binary, (self.lx, self.ly), 3, (0, 255, 0), -1)
        cv2.circle(right_binary, (self.rx, self.ry), 3, (0, 255, 0), -1)

        cv2.circle(crop_img, (self.lx, self.ly), 3, (0, 255, 0), -1)
        cv2.circle(crop_img, (self.rx+640, self.ry), 3, (0, 255, 0), -1)

        self.pub_commands()   

        # ====================================
        # cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("img", img)

        cv2.namedWindow("crop_img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("crop_img", crop_img)
                
        # cv2.namedWindow("poly_gone_image", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("poly_gone_image", polygone_img)

        # cv2.namedWindow("Image Threshholding", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("Image Threshholding", thresh_img)

        # cv2.namedWindow("line_only_image", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("line_only_image", line_only_image)

        cv2.namedWindow("left_binary", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("left_binary", left_binary)

        cv2.namedWindow("right_binary", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("right_binary", right_binary)
        
        cv2.waitKey(1)
        # ====================================

    def img_moment(self, data) :
        img = self.bridge.compressed_imgmsg_to_cv2(data)
        crop_img = img.copy()[self.crop_lower_y:self.crop_upper_y, :]
        blend_color = self.detect_color(crop_img)   # blend_color is HSV
     
        left_bc = blend_color.copy()[:, self.crop_lx_left:self.crop_rx_left, :]
        right_bc = blend_color.copy()[:, self.crop_lx_right:self.crop_rx_right, :]

        left_binary = self.binary_image(left_bc)
        right_binary = self.binary_image(right_bc)

        self.lx, self.ly, self.lflag, self.lcount = self.calculateMoment(left_binary)
        self.rx, self.ry, self.rflag, self.rcount = self.calculateMoment(right_binary)
        if self.rx == 0 :
            self.rx = self.cropImageWidth

        print(f'shape={left_binary.shape}, lx={self.lx}, ly={self.ly}, lflag={self.lflag}, lcount={self.lcount}')
        print(f'shape={right_binary.shape}, rx={self.rx}, ry={self.ry}, rflag={self.rflag}, rcount={self.rcount}')

        cv2.circle(left_bc, (self.lx, self.ly), 3, (0, 255, 0), -1)
        cv2.circle(right_bc, (self.rx, self.ry), 3, (0, 255, 0), -1)

        self.pub_commands()   

        # ====================================
        # cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("img", img)

        cv2.namedWindow("crop_img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("crop_img", crop_img)

        cv2.namedWindow("blend_color", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("blend_color", blend_color)
        
        cv2.namedWindow("left_bc", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("left_bc", left_bc)
        cv2.namedWindow("right_bc", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("right_bc", right_bc)
        
        cv2.waitKey(1)
        # ====================================

    def img_CB(self, data):
        self.img_momentHT(data)
        # self.img_moment(data)

if __name__ == '__main__' :
    try :
        camReg()
        rospy.spin()
    except rospy.ROSInterruptException :
        pass
