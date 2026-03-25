#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from geometry_msgs.msg import Twist

class Turtle_pub: #1. class 이름 설정
    def __init__(self): #2. init 단 설정
        rospy.init_node("turtle_pub_node") #1. node의 이름 설정
        self.pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=1) #2. node의 역할 설정
        self.cmd_msg = Twist()
        self.rate = rospy.Rate(1) #3-2. 주기 설정

    def func(self): #3. 함수 설정
        self.cmd_msg.linear.x = 1
        self.pub.publish(self.cmd_msg) #3-1. publish
        self.rate.sleep() #3-3. 주기 실행
        
def main(): #6. main() 함수 작성
    try:
        turtle_pub = Turtle_pub()
        while not rospy.is_shutdown():
            turtle_pub.func()
    except rospy.ROSInterruptException:
        pass

if __name__=="__main__":  #4.현재 구문을 작성함으로써, 현재 코드가 메인 코드임을 선언.
    main() #5. main() 함수 호출
    
            
            
