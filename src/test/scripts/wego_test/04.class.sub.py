#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from std_msgs.msg import Int32

class Class_sub: #1. class 이름 설정
    def __init__(self): #2. init 단 설정
        self.data = 0
        rospy.init_node("wego_sub_node") #1. node의 이름 설정
        rospy.Subscriber("/counter",Int32,callback=self.CB) #2. node의 역할 설정

    def CB(self,msg): #3. 콜백 함수 설정
        num = msg.data
        print(num)

def main():
    try:
        class_sub = Class_sub()
        rospy.spin() #4.스핀 설정
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":
    main()
    