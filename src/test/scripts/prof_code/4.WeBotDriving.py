#! /usr/bin/env python3

# -*- coding : utf-8 -*-

import rospy
import time
from ros_basics.msg import CamData,CamControl
from std_msgs.msg import Float64,Int64, Int32MultiArray
from cv_bridge import CvBridge
from math import *
import numpy as np

class WeBot_driving :
    def __init__(self):
        self.bridge = CvBridge()
        rospy.init_node("webot_ctrl_cmd_node")

        # Save Start time
        self.start_time = rospy.get_time()

        # 시뮬레이션 변수
        self.PubSpeed = rospy.Publisher("/commands/motor/speed",Float64,queue_size=3)
        self.PubAngle = rospy.Publisher("/commands/servo/position",Float64,queue_size=3)

        # Get /moment_pts topic from cal_moments publisher
        rospy.Subscriber("/moment_pts", Int32MultiArray, self.mpts_CB)

        self.speed_msg = Float64()
        self.steer_msg = Float64()

        # gps 변수
        # self.GpsSub = rospy.Subscriber("/sector",Int64,self.gpscallback)
        # self.gpsmsg = 0

        # For 1280 x 720 Camera Image Start ==============
        # self.imgWidth = 1280                     # image Width
        # self.imgHeight = 720                     # image Height
        # self.imgHalfWidth = self.imgWidth // 2   # image Half Width

        # # Default crop image size
        # self.cropImageWidth = 640
        # self.cropImageHeight = 200
        # For 1280 x 720 Camera Image end ==============

        # For 640 x 480 Camera Image Start ==============
        self.imgWidth = 640                     # image Width
        self.imgHeight = 480                     # image Height
        self.imgHalfWidth = self.imgWidth // 2   # image Half Width

        # Default crop image size
        self.cropImageWidth = 320
        self.cropImageHeight = 100
        # For 640 x 480 Camera Image end ==============


        # crop image for line detection
        self.cropOffsetWidth = 0            # offset X from left/right line for crop image
        self.cropOffsetHeight = 100         # offset Y from bottom line for crop image

        self.centerDist_crop = self.imgHalfWidth - self.cropImageWidth - self.cropOffsetWidth

        self.ref_dist = 50
        
        # Following line
        self.follow_line = 'R'

        self.lx = 160
        self.ly = 60
        self.rx = 160
        self.ry = 60

        # Regular execution with 10Hz
        rospy.Timer(rospy.Duration(1.0/10), self.timer_CB)
        
    def mpts_CB(self, data) :
        self.cropImageWidth = data.data[0]
        self.cropImageHeight = data.data[1]
        self.lx = data.data[2]
        self.ly = data.data[3]
        self.rx = data.data[4]
        self.ry = data.data[5]

    def timer_CB(self, _event) :
        self.Lane_follow_driving(600)

    def setRefDistance(self, refDist) :
        self.ref_dist = refDist

    def webotControl(self, steer, speed) :
        self.speed_msg.data = speed
        self.steer_msg.data = steer

        self.PubAngle.publish(self.steer_msg)
        self.PubSpeed.publish(self.speed_msg)

    def Stop(self) :
        self.speed_msg.data = 0
        self.steer_msg.data = 0.5

        self.PubAngle.publish(self.steer_msg)
        self.PubSpeed.publish(self.speed_msg)
        
    # Autonomous driving using moments point of lines
    # speed : 0 ~ 2400
    # steering : 0 ~ 0.5 ~ 1
    def Lane_follow_driving(self, speed=500) :
        # Save the current time
        self.end_time = rospy.get_time()

        # Send Control command in 10Hz 
        if self.end_time - self.start_time >= 0.1:
            self.start_time = self.end_time
            steering = 0

            # Steering angle (left:0 ~ 0.5, right:0.5 ~ 1): 0 ~ 0.5 ~ 1

            # validY = self.ly - self.ry
            # if validY < 10 :
            #     self.follow_line = 'B'
            # else :
            if 50 <= self.ry <= 60 :
                self.follow_line = 'R'
            elif 50 <= self.ly <= 60 :
                self.follow_line = 'L'

            if self.follow_line == 'R' :
                steering = (self.rx - 160) / speed + 0.5 
                print(f'rx={self.rx}, dist_from_center={self.rx - 160}, speed={speed}, steering={steering}')
            elif self.follow_line == 'L' :
                steering = (160 - self.lx) / speed + 0.5 
                print(f'rx={self.lx}, dist_from_center={160 - self.lx}, speed={speed}, steering={steering}')
            # elif self.follow_line == 'B' :
            #     # If left line is not detected, drive by right line.
            #     if (self.lx == 0) :
            #         if self.cropImageWidth - self.rx > self.ref_dist + 20 :
            #             steering = self.speed_steering[int(speed * 10)] 

            #     # If right line is not detected, drive by left line.
            #     elif (self.rx == self.cropImageWidth) :
            #         if self.lx > self.ref_dist + 20 :
            #             steering = -self.speed_steering[int(speed * 10)] 
            
            self.webotControl(steering, speed)

if __name__ == '__main__' :
    try :
        wb = WeBot_driving()
        wb.setRefDistance(50)
        rospy.spin()        
    except rospy.ROSInterruptException :
        pass