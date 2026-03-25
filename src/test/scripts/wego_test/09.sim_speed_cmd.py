#!/usr/bin/env python3
#-*-coding:utf-8-*-
import rospy
from std_msgs.msg import Float64

class Turtle_pub: #1. class 이름 설정
    def __init__(self): #2. init 단 설정
        rospy.init_node("sim_cmd_node") #1. node의 이름 설정
        self.pub = rospy.Publisher("/commands/motor/speed",Float64,queue_size=1) #2. node의 역할 설정
        self.cmd_msg = Float64()
        self.rate = rospy.Rate(100) #3-2. 주기 설정
        self.speed = 0

    def func(self): #3. 함수 설정
        self.speed += 1
        if self.speed >= 2400:
            self.speed = 2400
        self.cmd_msg.data = self.speed
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
    
            
            
