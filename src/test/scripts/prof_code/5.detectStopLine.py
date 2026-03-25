#!/usr/bin/env python3

import rospy
import roslib
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Int32MultiArray
from cv_bridge import CvBridge
from morai_msgs.msg import CtrlCmd, GetTrafficLightStatus
from smarp_msgs.msg import RecogObj, RoadInfo 

from math import *
import numpy as np
import cv2
from time import *


class StopLine :
    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node("Road_info")

        rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.img_CB)

        # lines, light, stopLine, labacorn, objects : True/False
        self.infoCtrl = rospy.Subscriber("/recog_objs",RecogObj, self.road_CB)
        
        # Status of objects recognization ============
        self.road_info = rospy.Publisher("/road_info", RoadInfo, queue_size=3)

        self.imgSizeX = 1280
        self.imgSizeY = 720

        # Range of ROI for Traffic Light (ERP42, K-City)
        # self.light_upper_left_pt = (200, 180)
        # self.light_lower_right_pt = (400, 280)

        # Range of ROI for Traffic Light (WeBot, KookMin)
        self.light_upper_left_pt = (300, 100)
        self.light_lower_right_pt = (860, 250)

        # Detected Light Color
        self.light_color = ''
        self.road_status = self.genRoadInfo()

        # Range of ROI for Stop Line
        self.stopLine_upper_left_pt = (400, 560)
        self.stopLine_lower_right_pt = (970, 620)

        self.start_time = rospy.get_time()

    def setLightROI(self, left_upper=(200,180), right_lower=(400,280)) :
        self.light_upper_left_pt = left_upper
        self.light_lower_right_pt = right_lower

    def genRoadInfo(self) :
        road_status = RoadInfo()
        road_status.light = 'U'
        road_status.stopline = False
        road_status.obj_no = 0
        road_status.obj_status = 'U'
        return road_status
          
    def detectStopLine(self, img) :
              
        sl_crop = img.copy()[self.stopLine_upper_left_pt[1]:self.stopLine_lower_right_pt[1], 
                                    self.stopLine_upper_left_pt[0]:self.stopLine_lower_right_pt[0]]
        
        _, L, _ = cv2.split(cv2.cvtColor(sl_crop, cv2.COLOR_BGR2HLS))
        _,L_roi = cv2.threshold(L,127,255,cv2.THRESH_BINARY)    

        h, w = L_roi.shape
        refCount = h * w * 0.7

        stopline_find = False
        if cv2.countNonZero(L_roi) > refCount:   
            self.road_status.stopline = True
        else:
            self.road_status.stopline = False

        self.road_info.publish(self.road_status)
        self.start_time = self.end_time

        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img", img)
        cv2.namedWindow("sl_crop", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("sl_crop", sl_crop)
        cv2.namedWindow("L", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("L", L)
        cv2.namedWindow("L_roi", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("L_roi", L_roi)
        print(f'shape of L={L_roi.shape}, stopline_find={self.road_status.stopline}')
        print(f'refCount={refCount}, stop line non zero count={cv2.countNonZero(L_roi)}')
        cv2.waitKey(1)

    def detectStopLine_canny(self, img) :
        sl_crop = img.copy()[self.stopLine_upper_left_pt[1]:self.stopLine_lower_right_pt[1], 
                             self.stopLine_upper_left_pt[0]:self.stopLine_lower_right_pt[0]]
        gray = cv2.cvtColor(sl_crop, cv2.COLOR_BGR2GRAY)
        
        blurred = cv2.GaussianBlur(gray, (5,5), 0)

        edges = cv2.Canny(blurred, 50, 150)
        lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

        print(f'lines={lines}')

        for line in lines :
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("img", img)
        cv2.namedWindow("sl_crop", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("sl_crop", sl_crop)
        cv2.namedWindow("blurred", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("blurred", blurred)
        cv2.namedWindow("edges", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("edges", edges)
        cv2.waitKey(1)


    def road_CB(self, data) :
        pass

    def img_CB(self, data) :
        img = self.bridge.compressed_imgmsg_to_cv2(data)

        self.imgSizeY, self.imgSizeX, _ = img.shape

        # print(f'img size={self.imgSizeX},{self.imgSizeY}')
        self.end_time = rospy.get_time()

        if (self.end_time - self.start_time > 0.1) :
            self.detectStopLine(img)
            self.start_time = self.end_time

            # self.traffic_light(img)
            # self.detectStopLine_canny(img)

if __name__ == '__main__' :
    try :
        StopLine()
        rospy.spin()
    except rospy.ROSInterruptException :
        pass


        