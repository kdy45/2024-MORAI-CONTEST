#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

rospy.init_node("wego_pub_node") #1. node의 이름 설정
pub = rospy.Publisher("/counter",Int32,queue_size=1) #2. node의 역할 설정
int_msg = Int32()
rate = rospy.Rate(1) #3-2. 주기 설정

num = 0
while not rospy.is_shutdown():
    num = num+1
    int_msg.data = num
    pub.publish(int_msg) #3-1. publish
    print(num)
    rate.sleep() #3-3. 주기 실행