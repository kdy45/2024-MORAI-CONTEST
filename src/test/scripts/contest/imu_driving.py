#!/usr/bin/env python3

'''
https://copyprogramming.com/howto/subscribe-to-imu-sensor-and-monitor-the-orientation-value-to-determine-the-driving-direction-of-the-car
'''

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64,Int64, Int32MultiArray
from tf.transformations import euler_from_quaternion
from time import time

import math

import numpy as np
import os

# orientation :
#  - z, w : meaningless
#  - x : 0.00087
#  - y : 0.002055
# angular velocity
#  - x : 
#  - y
#  - 

class imuDriving :
    DIRECTION_UNKNOWN = -10
    DIRECTION_LEFT = -1
    DIRECTION_STRAIGHT = 0
    DIRECTION_RIGHT = 1

    DIRECTION_DEF = {
        DIRECTION_UNKNOWN: "unknown",
        DIRECTION_LEFT: "left",
        DIRECTION_STRAIGHT: "straight",
        DIRECTION_RIGHT: "right"
    }

    def __init__(self, timeout_in_s= 2.0) :
        rospy.init_node('imu_driving', anonymous=True)    
        self.imu_sub = rospy.Subscriber("/imu", Imu, self.imu_CB)

        self.PubSpeed = rospy.Publisher("/commands/motor/speed",Float64,queue_size=3)
        self.PubAngle = rospy.Publisher("/commands/servo/position",Float64,queue_size=3)
        self.const_timeout_in_s = timeout_in_s      
        self.imu_msg = Imu()
        self.last_yaw = self.get_current_yaw()
        self.target_yaw_diff = math.pi / 2
        self.rotation_done = False
        self.turn_start_flag = True
        self.last_time = rospy.get_time()

        rospy.Timer(rospy.Duration(1.0/10), self.imu_timer_CB)

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
        print(f'rotation_done:{self.rotation_done}, self.turn_start_flag={self.turn_start_flag}, self.target_yaw_diff={self.target_yaw_diff}')
        if not self.rotation_done :
            self.left_turn()
   

    #     # IMU 타이머 CallBack 함수. 회전이 완료되지 않으면 <left_turn>함수를 호출해 회전시킴
    # def imu_timer_CB(self, _event) :
    #     # os.system("clear")
    #     print(f'rotation_done:{self.rotation_done}, self.turn_start_flag={self.turn_start_flag}, self.target_yaw_diff={self.target_yaw_diff}')
    #     if not self.rotation_done :
    #         self.left_turn()
   
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

        print(f'yaw_current={yaw_current}, last_yaw={self.last_yaw}, target_yaw_diff={self.target_yaw_diff}')

        if abs(yaw_current - self.last_yaw) >= self.target_yaw_diff :
            self.rotation_done = True
            
        # print(f'rotation deg={(yaw_current - self.last_yaw)*180/math.pi}')
            
if __name__ == '__main__':
    try:
        det_driving_dir = imuDriving()
        rospy.spin()    
    except rospy.ROSInterruptException:
        pass    
