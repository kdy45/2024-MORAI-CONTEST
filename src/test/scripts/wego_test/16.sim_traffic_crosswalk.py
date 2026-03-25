#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from morai_msgs.msg import GetTrafficLightStatus
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float64
from cv_bridge import CvBridge
import cv2
import numpy as np
from time import *

class Traffic_control:
    def __init__(self):
        rospy.init_node("lane_sub_node")
        self.steer_pub = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        self.speed_pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        rospy.Subscriber("/GetTrafficLightStatus",GetTrafficLightStatus,self.traffic_CB)
        rospy.Subscriber("/image_jpeg/compressed",CompressedImage,self.cam_CB)
        self.bridge = CvBridge()
        self.steer_msg = Float64()
        self.speed_msg = Float64()
        self.traffic_msg = GetTrafficLightStatus()
        self.traffic_flag = 0
        self.prev_signal = 0
        self.signal = 0
        self.cross_flag = 0
        self.img = []
        self.img_flag = 0
        self.center_index = 0
        self.standard_line = 0
        self.degree_per_pixel = 0
        
        
    def traffic_CB(self,msg):
        self.traffic_msg = msg
        if self.traffic_msg.trafficLightIndex == "SN000002":
            self.signal = self.traffic_msg.trafficLightStatus
            if self.prev_signal != self.signal:
                self.prev_signal = self.signal
            self.traffic_think()
            
    def traffic_think (self):
        if self.signal == 1:
            pass
            #print("red")
        elif self.signal == 4:
            pass
            #print("yellow")
        elif self.signal == 16:
            pass
            #print("green")
        elif self.signal == 33:
            pass
            #print("left")
        else:
            pass


    def cam_CB(self,msg):
        self.img = self.bridge.compressed_imgmsg_to_cv2(msg)
        self.warped_img,self.center_index, self.standard_line, self.degree_per_pixel = self.cam_lane_detection()

    def cam_lane_detection(self):    
        y,x = self.img.shape[0:2]
        img_hsv = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(img_hsv)

        yellow_lower = np.array([15,128,0])
        yellow_upper = np.array([40,255,255])
        yellow_range = cv2.inRange(img_hsv,yellow_lower,yellow_upper)
        white_lower = np.array([0,0,192])
        white_upper = np.array([179,64,255])
        white_range = cv2.inRange(img_hsv,white_lower,white_upper)
        combined_range = cv2.bitwise_or(yellow_range,white_range)
        filtered_img = cv2.bitwise_and(self.img,self.img,mask=combined_range)
        src_point1 = [0,420]
        src_point2 = [275,260]
        src_point3 = [x - 275,260]
        src_point4 = [x,420]
        src_points = np.float32([src_point1,src_point2,src_point3,src_point4])

        dst_point1 = [x//8,480]
        dst_point2 = [x//8,0]
        dst_point3 = [x//8*7,0]
        dst_point4 = [x//8*7,480]
        dst_points = np.float32([dst_point1,dst_point2,dst_point3,dst_point4])

        matrix = cv2.getPerspectiveTransform(src_points,dst_points)
        warped_img = cv2.warpPerspective(filtered_img,matrix,[x,y])
        grayed_img = cv2.cvtColor(warped_img,cv2.COLOR_BGR2GRAY)
        bin_img = np.zeros_like(grayed_img)
        bin_img[grayed_img>50] = 1
        histogram_x = np.sum(bin_img,axis=0)
        histogram_y = np.sum(bin_img,axis=1)

        left_hist = histogram_x[0:x//2]
        right_hist = histogram_x[x//2:]
        up_hist = histogram_y[0:y//4*3]
        down_hist = histogram_y[y//4*3:]
        left_indices = np.where(left_hist>20)[0]
        right_indices = np.where(right_hist>20)[0]+320
        cross_indices = np.where(down_hist>480)[0]+y//4*3
        #print(histogram_y)
        try:
            cross_threshold = 25
            cross_diff = cross_indices[-1] - cross_indices[0]
            if cross_threshold < cross_diff:
                self.cross_flag = True
                cv2.rectangle(warped_img,[0,cross_indices[0]],[x,cross_indices[-1]],[0,255,0],3)
            else:
                self.cross_flag - False
        except:
            self.cross_flag = False
      
        indices = np.where(histogram_x>20)[0]
        try:
            if len(left_indices)!=0 and len(right_indices)!=0:
                center_index = (indices[0]+indices[-1])//2
                #print("both_line")
            elif len(left_indices)!=0 and len(right_indices)==0:
                center_index = (left_indices[0]+left_indices[-1])//2
                #print("left_line")
            elif len(left_indices)==0 and len(right_indices)!=0:
                center_index = (right_indices[0]+right_indices[-1])//2
                #print("right_line")
        except:
            center_index = x//2
            #print("no_line")

        standard_line = x//2
        degree_per_pixel = 1/x
        return warped_img,center_index, standard_line, degree_per_pixel

    def action(self):
        if len(self.img) != 0:
            if self.cross_flag == True and self.signal == 1:
                speed = 0
                steer = 0.5
            else:
                steer = (self.center_index - self.standard_line) * self.degree_per_pixel
                steer = 0.5+steer
                speed = 1000

            self.steer_msg.data = steer
            self.speed_msg.data = speed
            self.speed_pub.publish(self.speed_msg)
            self.steer_pub.publish(self.steer_msg)
            #cv2.imshow("canny_img",canny_img)
            cv2.imshow("img",self.img)
            cv2.imshow("warped_img",self.warped_img)
            cv2.waitKey(1)

def main():
    try:
        traffic_control = Traffic_control()
        while not rospy.is_shutdown():
            traffic_control.action()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()    