#! /usr/bin/env python3

# -*- coding : utf-8 -*-

import rospy
import time
from std_msgs.msg import Float64,Int64, Int32MultiArray, Bool
from smarp_msgs.msg import camInfo, recogObj, objectStatus, objInfo, lidarStatus
from morai_msgs.msg import CtrlCmd, GetTrafficLightStatus
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from cv_bridge import CvBridge
import math 
import numpy as np
import os

class ModelS_Driving :
    def __init__(self) :
        self.bridge = CvBridge()
        rospy.init_node("models_driving_noslam")

        self.start_time = rospy.get_time()
        
        rospy.Subscriber("/GetTrafficLightStatus",GetTrafficLightStatus,self.traffic_CB)
        self.imu_sub = rospy.Subscriber("/imu", Imu, self.imu_CB)

        self.PubSpeed = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1)
        self.speed_msg = Float64()

        self.PubAngle = rospy.Publisher("/commands/servo/position",Float64,queue_size=1)
        self.steer_msg = Float64()

        self.PubReg = rospy.Publisher("/recog_objs", recogObj, queue_size=1)
        self.reg_msg = recogObj()

        self.subCam = rospy.Subscriber("/cam_info", camInfo, self.cam_CB)
        
        rospy.Subscriber("/moment_pts", Int32MultiArray, self.mpts_CB)
        
        self.imgSizeX = 640
        self.imgSizeY = 480    
        
        self.cam_msg = camInfo()
        self.lx = 160
        self.ly = 60
        self.rx = 160
        self.ry = 60

        self.dx = 160
        self.dy = 60
        self.fx = 160
        self.fy = 60

        # Range of ROI for Stop Line
        self.stopLine_upper_left_pt = (70, 400)
        self.stopLine_lower_right_pt = (500, 480)

        self.subLidar = rospy.Subscriber("/obj_scan", objectStatus, self.lidar_CB)
        self.pubLidar = rospy.Publisher("/lidar_range", lidarStatus, queue_size=1)
        self.lidar_msg = objectStatus()
        self.lidar_stat_msg = lidarStatus()
        self.no_objects = 0
        self.objects = objInfo()

        rospy.Subscriber("/slam_end", Bool, self.slam_CB)
        
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
        self.signal = 0
        self.stopLine = 0
        self.stopLine_flag = False
        self.prev_signal = 0
        self.centerDist_crop = self.imgHalfWidth - self.cropImageWidth - self.cropOffsetWidth
        self.ref_dist = 50

        self.rotation_angle = 0

        self.imu_msg = Imu()
        self.last_yaw = self.get_current_yaw()
        self.target_yaw_diff = math.pi / 2
        self.rotation_done = False
        self.turn_start_flag = False
        self.last_time = rospy.get_time()
        
        # 미션 번호 
        #   1 : SLAM
        #   2 : 동적/정적 미션
        #   3 : 동적/정적 미션
        #   4 : 회전교차로 미션
        #   5 : 신호등 미션
        
        self.mode = 1

        # Following line
        self.follow_line = 'R'

        # Regular execution with 10Hz
        rospy.Timer(rospy.Duration(1.0/10), self.timer_CB)

    def traffic_CB(self,msg):
        self.traffic_msg = msg
        if self.traffic_msg.trafficLightIndex == "SN000005":
            self.signal = self.traffic_msg.trafficLightStatus
        
           
        else: 
            pass

    def cam_CB(self, msg) :
        # self.cam_msg = msg
        self.stopLine = msg.stopline
        if self.stopLine == True :
            self.stopLine_flag = True
            rospy.loginfo(f"{self.stopLine_flag}")
        self.cropImageWidth = msg.crop_image_width
        self.cropImageHeight = msg.crop_image_height
        self.dx = msg.m_lx
        self.dy = msg.m_ly
        self.fx = msg.m_rx
        self.fy = msg.m_ry
        #print(f'cam msg={msg}')
    
    def mpts_CB(self, msg) :
        self.cam_msg = msg
        self.cropImageWidth = msg.data[0]
        self.cropImageHeight = msg.data[1]
        self.lx = msg.data[2]
        self.ly = msg.data[3]
        self.rx = msg.data[4]
        self.ry = msg.data[5]

    def lidar_CB(self, msg) :
        self.lidar_msg = msg
        self.no_objects = msg.no_objects
        self.objects = msg.objects
        # print(f'lidar_msg={self.lidar_msg}')

    # 현재 z축을 나타냄(쿼터니언을 오일러 각도로 변환하여 yaw 값을 반환)
    def get_current_yaw(self) :
        quaternion_list = [self.imu_msg.orientation.x, self.imu_msg.orientation.y, 
                           self.imu_msg.orientation.z, self.imu_msg.orientation.w]
        euler_list = euler_from_quaternion(quaternion_list)
        return euler_list[2]  

    # IMU CallBack 함수. 받은 메세지를 imu_msg에 저장
    def imu_CB(self, msg):
        # os.system("clear")
        self.imu_msg = msg
        # print(f'rotation_done:{self.rotation_done}, self.turn_start_flag={self.turn_start_flag}, self.target_yaw_diff={self.target_yaw_diff}')
        if not self.rotation_done :
            self.left_turn()

    # <drive_by_imu>함수를 호출해 주어진 방향으로 차량을 주행시킴
    def left_turn(self) :
        if not self.rotation_done :
            if self.turn_start_flag :
                self.last_yaw = self.get_current_yaw()
                self.turn_start_flag = False
            
            self.drive_by_imu()
   
    # 현재 yaw각도를 확인 후 목표 yaw 각도 변화량에 도달하면 rotation_done을 TRUE로 설정해 회전이 완료되었음을 출력
    def drive_by_imu(self) :
        yaw_current = self.get_current_yaw()

        # print(f'yaw_current={yaw_current}, last_yaw={self.last_yaw}, target_yaw_diff={self.target_yaw_diff}')

        if abs(yaw_current - self.last_yaw) >= self.target_yaw_diff :
            self.rotation_done = True
    
    def slam_CB(self, msg) :
        self.slam_end_flag = msg.data

    # 미션 번호 
    #   1 : SLAM
    #   2 : 동적/정적 미션
    #   3 : 동적/정적 미션
    #   4 : 회전교차로 미션
    #   5 : 신호등 미션
    
    def timer_CB(self,event) :
        if self.mode == 1 : # 정적/동적 판단 후 회피 
            self.Lane_follow_driving(600)
            if self.no_objects == 1:
                self.Stop()
                try:
                    self.pre_obs_deg_left = self.objects[0].deg[-1]
                    self.pre_obs_deg_right = self.objects[0].deg[0]
                    start_time = rospy.get_time()
                    end_time = 0

                    while True:
                        end_time = rospy.get_time()
                        # print(end_time)
                        if end_time - start_time >= 1:
                            break
                    self.obs_deg_left = self.objects[0].deg[-1]
                    self.obs_deg_right = self.objects[0].deg[0]
                    self.Object_type_decision()
                    
                except IndexError:
                    pass
 
            elif self.traffic_msg.trafficLightIndex == "SN000009" and self.ly == 0:
                # self.turn_start_flag = True
                print(f"왼쪽 차선이 없습니다.")
                self.turnA()
                self.mode = 2
                self.lidar_range_change(90,270,5)
            
            else:
                pass
                
        elif self.mode == 2 :
            self.Lane_follow_driving(500)
            if self.no_objects >= 1 and self.stopLine == True:
                self.lidar_range_change(155,270,1)
                while True :
                    self.Stop()    
                    if self.no_objects == 0:
                        self.turnB()
                        self.follow_line = 'L'
                        self.lidar_range_change(181,179,0.01)
                        break   

            elif self.follow_line == 'L' and self.stopLine == True and self.signal == 33 :
                self.turn_traffic()
                self.signal = 0
                rospy.loginfo(f"{self.signal}")
            
            elif self.follow_line == 'L' and self.stopLine == True and (self.signal == 16 or self.signal == 1 or self.signal == 4 or self.signal == 5) :
                self.stopLineaction()
                self.signal = 0
                rospy.loginfo(f"{self.signal}")

            elif self.signal == 0 and self.stopLine and self.follow_line == 'L' :
                print("ok")
                self.Stop()
                start_time = rospy.get_time()
                end_time = rospy.get_time()
                while end_time - start_time <= 1 :
                    end_time = rospy.get_time()
                self.turn_right()
                self.signal = 100
            
            elif self.traffic_msg.trafficLightIndex == 'SN000000' and self.stopLine and self.follow_line == 'L' :
                print("last straight")
                start_time = rospy.get_time()
                end_time = rospy.get_time()
                while end_time - start_time <= 2 :
                    end_time = rospy.get_time()
                    self.webotControl(0.455,500)
                while self.traffic_msg.trafficLightIndex != 'SN000009' :
                    self.webotControl(0.5,500)

            else :
                pass
    
    def lidar_range_change(self, rightrange, leftrange, dist) :
        self.lidar_stat_msg.range = [rightrange,leftrange]
        self.lidar_stat_msg.dist = dist
        self.pubLidar.publish(self.lidar_stat_msg)

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

    def Object_type_decision(self) :
        if self.obs_deg_left - self.pre_obs_deg_left <= 3 and self.obs_deg_right - self.pre_obs_deg_right <= 3:  # 정적 장애물
            print("static")
            # self.turn_t = rospy.get_time()
            # self.t2 = rospy.get_time()
            self.Lane_change()
        
        elif self.obs_deg_left - self.pre_obs_deg_left > 6 or self.obs_deg_right - self.pre_obs_deg_right > 6:  #동적 장애물
            print("dynamic")  
            while self.no_objects == 1:
                self.Stop()
                if self.no_objects == 0:
                    pass

        else:
            pass

    def Lane_change(self) :
        while self.no_objects == 1:
            self.webotControl(0,150)

        self.turn_t = rospy.get_time() 
        self.t2 = rospy.get_time()

        while self.t2 - self.turn_t <= 2.65:
            self.webotControl(0.83,400)
            self.t2 = rospy.get_time()
      
    # 로터리 전 좌회전  
    def turnA(self):
        self.rotation_angle = 0.19
        print(f"현재 회전 각도: {self.rotation_angle}")
        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 4 :
            end_time = rospy.get_time()
            self.webotControl(self.rotation_angle, speed = 300)
            
        self.rotation_angle = self.rotation_angle + 0.06

        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 3 :
            end_time = rospy.get_time()
            # rospy.loginfo("회전 중 오른쪽에 실선이 보임. 회전을 멈추고 차선인식 주행")
            # print(f"2초후 회전 각도: {self.rotation_angle}")
            self.webotControl(self.rotation_angle, speed = 300)
        self.webotControl(steer = 0.7, speed = 300)

    # 로터리 회전
    def turnB(self) :
        rospy.loginfo('turnB')         
        self.rotation_angle = 0.8
        print(f"현재 회전 각도: {self.rotation_angle}")
        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 2 :
            end_time = rospy.get_time()
            self.webotControl(self.rotation_angle, speed = 300)
            
        self.rotation_angle = self.rotation_angle - 0.06

        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 6 :
            end_time = rospy.get_time()
            # print(f"2초후 회전 각도: {self.rotation_angle}")
            self.webotControl(self.rotation_angle, speed = 300)
        self.webotControl(steer = 0.7, speed = 300)

    # 교차로 좌회전
    def turn_traffic(self):
        # self.rotation_angle = 0.28
        self.rotation_angle = 0.273
        print(f"현재 회전 각도: {self.rotation_angle}")
        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 5 :
            end_time = rospy.get_time()
            self.webotControl(self.rotation_angle, speed = 500)
            
        self.rotation_angle = self.rotation_angle - 0.2
        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 2 :
            end_time = rospy.get_time()
        if self.ly == 1 :    
            self.Lane_follow_driving(500)

    # 교차로 회전 후 우회전
    def turn_right(self):
        self.rotation_angle = 0.5
        print(f"현재 회전 각도: {self.rotation_angle}")
        start_time = rospy.get_time()
        end_time = rospy.get_time()
        while end_time - start_time <= 3 :
            end_time = rospy.get_time()
            self.webotControl(self.rotation_angle, speed = 300)

        self.rotation_angle = self.rotation_angle + 0.425
        start_time = rospy.get_time()
        end_time = rospy.get_time()

        while end_time - start_time <= 5 :
            end_time = rospy.get_time()
            self.webotControl(self.rotation_angle, speed = 300)
               
    def stopLineaction(self) :
        while True :
            if self.signal == 33:
                self.turn_traffic()
                break
            else:       
                self.webotControl(0.5,0)
    
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

            # if 50 <= self.ry <= 60 :
            #     self.follow_line = 'R'
            # elif 50 <= self.ly <= 60 :
            #     self.follow_line = 'L'
            # else :
                # self.follow_line = 'N'

            if self.follow_line == 'R' :
                steering = (self.rx - 210) / speed + 0.5 
                # print(f'rx={self.rx}, dist_from_center={self.rx - 180}, speed={speed}, steering={steering}')
            elif self.follow_line == 'L' :
                steering = (self.lx - 80) / speed + 0.5 
                # print(f'rx={self.lx}, dist_from_center={180 - self.lx}, speed={speed}, steering={steering}')
            else :
                steering = 0.5
            
            if self.detect_corner_speed():
                speed = 400
           
            self.webotControl(steering, speed)
            
    def detect_corner_speed(self):
        #if self.rx - self.lx > 57:
        if self.rx < 125 or self.lx > 190:
            return True
        else:
            return False

if __name__ == '__main__' :
    try :
        wb = ModelS_Driving()
        wb.setRefDistance(50)
        rospy.spin()        
    except rospy.ROSInterruptException :
        pass
