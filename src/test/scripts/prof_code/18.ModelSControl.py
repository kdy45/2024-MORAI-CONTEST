#! /usr/bin/env python3

# -*- coding : utf-8 -*-

import rospy
import time
from std_msgs.msg import Float64,Int64, Int32MultiArray
from smarp_msgs.msg import camInfo, recogObj, objectStatus, objInfo
from math import *
import numpy as np

class ModelS_Driving :
    def __init__(self) :
        rospy.init_node("models_driving")

        self.PubSpeed = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.speed_msg = Float64()

        self.PubAngle = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        self.steer_msg = Float64()

        self.PubReg = rospy.Publisher("/recog_ctrl_cmd", recogObj, queue_size=1 )
        self.reg_msg = recogObj()

        self.subCam = rospy.Subscriber("/cam_mnt", camInfo, self.cam_CB)
        self.cam_msg = camInfo()
        self.lx = 160
        self.ly = 60
        self.rx = 160
        self.ry = 60

        self.subLidar = rospy.Subscriber("/obj_scan", objectStatus, self.lidar_CB)
        self.lidar_msg = objectStatus()
        self.no_objects = 0
        self.objects = objInfo()
        
        # 미션 번호 
        #   1 : SLAM
        #   2 : 동적/정적 미션
        #   3 : 동적/정적 미션
        #   4 : 회전교차로 미션
        #   5 : 신호등 미션
        self.mission_no = 1

        # Following line
        self.follow_line = 'R'

        # Regular execution with 10Hz
        rospy.Timer(rospy.Duration(1.0/10), self.timer_CB)


    def cam_CB(self, msg) :
        self.cam_msg = msg
        self.lx = msg.m_lx
        self.ly = msg.m_ly
        self.rx = msg.m_rx
        self.ry = msg.m_ry
        print(f'cam msg={msg}')


    def lidar_CB(self, msg) :
        self.lidar_msg = msg
        self.no_objects = msg.no_objects
        self.objects = msg.objects

        print(f'lidar_msg={self.lidar_msg}')

    # 미션 번호 
    #   1 : SLAM
    #   2 : 동적/정적 미션
    #   3 : 동적/정적 미션
    #   4 : 회전교차로 미션
    #   5 : 신호등 미션
    def timer_CB(self) :
        if self.mission_no == 1 :                           # SLAM
            pass
        elif self.mission_no == 2 or self.mission_no == 3 : # 물체가 1개 인식된 경우 --> 정적/동적 판단 후, 로터리 주행
            pass
        elif self.mission_no == 4 :                         # 회전 교차로
            pass
        elif self.mission_no == 5 :                         # 신호등
            pass
       
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

    def Object_type_decision(self) :
        pass

    def Lane_change(self) :
        pass

    def turnAction(self, degree) :
        pass

    def detectTrafficeLight(self) :
        pass
    


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

            if 50 <= self.ry <= 60 :
                self.follow_line = 'R'
            elif 50 <= self.ly <= 60 :
                self.follow_line = 'L'
            else :
                self.follow_line = 'N'

            if self.follow_line == 'R' :
                steering = (self.rx - 160) / speed + 0.5 
                # print(f'rx={self.rx}, dist_from_center={self.rx - 160}, speed={speed}, steering={steering}')
            elif self.follow_line == 'L' :
                steering = (160 - self.lx) / speed + 0.5 
                # print(f'rx={self.lx}, dist_from_center={160 - self.lx}, speed={speed}, steering={steering}')
            else :
                steering = 0.5
           
            self.webotControl(steering, speed)

if __name__ == '__main__' :
    try :
        wb = ModelS_Driving()
        wb.setRefDistance(50)
        rospy.spin()        
    except rospy.ROSInterruptException :
        pass
