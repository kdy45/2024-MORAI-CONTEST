import rospy
from cv_bridge import CvBridge
from std_msgs.msg import Float64
import cv2
import numpy as np

class webotDrivingTest :
    def __init__(self) :
        rospy.init_node("webot_driving")
        self.PubSpeed = rospy.Publisher("/commands/motor/speed", Float64, queue_size=1)
        self.PubAngle = rospy.Publisher("/commands/servo/position", Float64, queue_size=1)

        self.speed_msg = Float64()
        self.steer_pub = Float64()

    def driveTest(self, angle, speed) :
        while (True) :
            self.PubAngle.publish(angle)
            self.PubSpeed.publish(speed)
        
if __name__ == '__main__' :
    try :
        traffic_control = webotDrivingTest()
        traffic_control.driveTest(10, 1000)
        rospy.spin()
    except rospy.ROSInterruptException :
        pass

