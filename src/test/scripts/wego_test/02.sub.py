#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

def CB(msg): #3. 콜백 함수 설정
    num = msg.data
    print(num)

rospy.init_node("wego_sub_node") #1. node의 이름 설정
rospy.Subscriber("/counter",Int32,callback=CB) #2. node의 역할 설정
rospy.spin() #4.스핀 설정

