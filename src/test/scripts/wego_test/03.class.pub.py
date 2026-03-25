#!/usr/bin/env python3
#-*-coding:utf-8-*-

import rospy
from std_msgs.msg import Int32

class Class_pub: #1. class 이름 설정
    def __init__(self): #2. init 단 설정
        rospy.init_node("wego_pub_node") #1. node의 이름 설정
        self.pub = rospy.Publisher("/counter",Int32,queue_size=1) #2. node의 역할 설정
        self.int_msg = Int32()
        self.rate = rospy.Rate(1) #3-2. 주기 설정

    def func(self): #3. 함수 설정
        num = 0
        while not rospy.is_shutdown():
            num = num+1
            self.int_msg.data = num
            self.pub.publish(self.int_msg) #3-1. publish
            print(num)
            self.rate.sleep() #3-3. 주기 실행
            

def main():
    try:
        class_name = Class_pub()
        class_name.func()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()