#! /usr/bin/env python3

import rospy    

from std_msgs.msg import Bool
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
import actionlib

class NavigationClient:
    def __init__(self):
        self.slam_end_pub = rospy.Publisher("/slam_end", Bool, queue_size=1)
        self.client=actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.client.wait_for_server()
        
        self.end_flag = Bool()
        self.goal_list = list()
        
        self.waypoint_1 = MoveBaseGoal()
        self.waypoint_1.target_pose.header.frame_id='map'
        self.waypoint_1.target_pose.pose.position.x = 2.86512185661
        self.waypoint_1.target_pose.pose.position.y = -3.08288871199
        self.waypoint_1.target_pose.pose.orientation.w =  0.7144673727
        self.waypoint_1.target_pose.pose.orientation.z = -0.6996687596
        
        self.goal_list.append(self.waypoint_1)
        
        self.waypoint_2 = MoveBaseGoal()
        self.waypoint_2.target_pose.header.frame_id='map'
        self.waypoint_2.target_pose.pose.position.x = 2.86512185661
        self.waypoint_2.target_pose.pose.position.y = -3.08288871199
        self.waypoint_2.target_pose.pose.orientation.w =  0.7144673727
        self.waypoint_2.target_pose.pose.orientation.z = -0.6996687596
        
        self.goal_list.append(self.waypoint_2)
        
        self.waypoint_4 = MoveBaseGoal()
        self.waypoint_4.target_pose.header.frame_id='map'
        self.waypoint_4.target_pose.pose.position.x =5.1632915258
        self.waypoint_4.target_pose.pose.position.y = -4.98950200673
        self.waypoint_4.target_pose.pose.orientation.w =0.794038624388
        self.waypoint_4.target_pose.pose.orientation.z = 0.60786730704
        
        self.goal_list.append(self.waypoint_4)
        
      
        # self.waypoint_6 = MoveBaseGoal()
        # self.waypoint_6.target_pose.header.frame_id='map'
        # self.waypoint_6.target_pose.pose.position.x =   5.52326246202
        # self.waypoint_6.target_pose.pose.position.y =-3.3317105753
        # self.waypoint_6.target_pose.pose.orientation.w =  0.72511585116
        # self.waypoint_6.target_pose.pose.orientation.z =  0.68862689635
        
        # self.goal_list.append(self.waypoint_6)
        
        self.waypoint_6 = MoveBaseGoal()
        self.waypoint_6.target_pose.header.frame_id='map'
        self.waypoint_6.target_pose.pose.position.x =   5.546958157589
        self.waypoint_6.target_pose.pose.position.y =-3.5308542440935
        self.waypoint_6.target_pose.pose.orientation.w = 0.699360857029
        self.waypoint_6.target_pose.pose.orientation.z =  0.71476876796227
        
        self.goal_list.append(self.waypoint_6)
        
        
        
        self.waypoint_7 = MoveBaseGoal()
        self.waypoint_7.target_pose.header.frame_id='map'
        self.waypoint_7.target_pose.pose.position.x =  5.99798972
        self.waypoint_7.target_pose.pose.position.y = -1.68005602860
        self.waypoint_7.target_pose.pose.orientation.w =0.95156823482
        self.waypoint_7.target_pose.pose.orientation.z = 0.3074376269698
        self.goal_list.append(self.waypoint_7)
        
        self.waypoint_8 = MoveBaseGoal()
        self.waypoint_8.target_pose.header.frame_id='map'
        self.waypoint_8.target_pose.pose.position.x =  9.114750873618
        self.waypoint_8.target_pose.pose.position.y = -2.416797081278
        self.waypoint_8.target_pose.pose.orientation.w = 0.99465800490317
        self.waypoint_8.target_pose.pose.orientation.z = -0.103225255059
        
        self.goal_list.append(self.waypoint_8)
    
        self.waypoint_11= MoveBaseGoal()
        self.waypoint_11.target_pose.header.frame_id='map'
        self.waypoint_11.target_pose.pose.position.x = 12.165038544458
        self.waypoint_11.target_pose.pose.position.y = -4.370149839331
        self.waypoint_11.target_pose.pose.orientation.w =  0.9096052504730
        self.waypoint_11.target_pose.pose.orientation.z = -0.4154735711352
        
        self.goal_list.append(self.waypoint_11)
        
        self.waypoint_13 = MoveBaseGoal()
        self.waypoint_13.target_pose.header.frame_id='map'
        self.waypoint_13.target_pose.pose.position.x =12.5633158996
        self.waypoint_13.target_pose.pose.position.y = -7.5225041898712
        self.waypoint_13.target_pose.pose.orientation.w = 0.71090948664
        self.waypoint_13.target_pose.pose.orientation.z = -0.7032835145
        
        self.goal_list.append(self.waypoint_13)
        
        
        self.waypoint_26 = MoveBaseGoal()
        self.waypoint_26.target_pose.header.frame_id='map'
        self.waypoint_26.target_pose.pose.position.x =13.829462758
        self.waypoint_26.target_pose.pose.position.y = -8.7283702060
        self.waypoint_26.target_pose.pose.orientation.w = 0.99901202512
        self.waypoint_26.target_pose.pose.orientation.z = -0.04444067577
        
        self.goal_list.append(self.waypoint_26)
        
        self.waypoint_31 = MoveBaseGoal()
        self.waypoint_31.target_pose.header.frame_id='map'
        self.waypoint_31.target_pose.pose.position.x =17.9313586
        self.waypoint_31.target_pose.pose.position.y = -9.71359916
        self.waypoint_31.target_pose.pose.orientation.w = 0.9999803
        self.waypoint_31.target_pose.pose.orientation.z = 0.0090421107
        self.goal_list.append(self.waypoint_31)
        
        self.waypoint_33 = MoveBaseGoal()
        self.waypoint_33.target_pose.header.frame_id='map'
        self.waypoint_33.target_pose.pose.position.x= 19.7892818094
        self.waypoint_33.target_pose.pose.position.y =-9.7123058334544
        self.waypoint_33.target_pose.pose.orientation.w =0.9999977502115
        self.waypoint_33.target_pose.pose.orientation.z = 0.0021212194119415
        
        self.goal_list.append(self.waypoint_33)
        
        self.waypoint_34 = MoveBaseGoal()
        self.waypoint_34.target_pose.header.frame_id='map'
        self.waypoint_34.target_pose.pose.position.x =19.68
        self.waypoint_34.target_pose.pose.position.y = -10.29
        self.waypoint_34.target_pose.pose.orientation.w = 0.99
        self.waypoint_34.target_pose.pose.orientation.z = -0.013
        
        self.goal_list.append(self.waypoint_34)


        self.sequence = 0
        self.start_time = rospy.Time.now()
        self.num_goals = len(self.goal_list)
        
        self.end_flag = False

    def run(self):
        current_time = rospy.Time.now()
        elapsed_time = (current_time - self.start_time).to_sec()

        if self.client.get_state() != GoalStatus.ACTIVE:
            self.start_time = rospy.Time.now()
            self.sequence = (self.sequence + 1) % self.num_goals

            if self.sequence == self.num_goals - 1:  # 마지막 목표에 도달하면
                self.stop()
            else:
                rospy.loginfo(f'Sending goal {self.sequence + 1}/{self.num_goals}')
                self.client.send_goal(self.goal_list[self.sequence])

    def stop(self):
        self.end_flag = True
        self.slam_end_pub.publish(self.end_flag)
        self.client.cancel_all_goals()
        rospy.loginfo('All goals completed. Stopping the node.')
        rospy.signal_shutdown("all goals completed")

def main():
    rospy.init_node('navigation_client')
    nc = NavigationClient()
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        nc.run()
        rate.sleep()

if __name__ == '__main__':
    main()
#         self.sequence = 0
#         self.start_time = rospy.Time.now()
#         self.num_goals = len(self.goal_list)
        
#         GoalStatus.ACTIVE = False

        
#     def run(self):
#         if self.client.get_state() != GoalStatus.ACTIVE:
#             # self.start_time = rospy.Time.now()
#             self.sequence = (self.sequence + 1) % self.num_goals
#             print(f'1-client.state={self.client.get_state()},GoalStatus.ACTIVE={GoalStatus.ACTIVE}, sequence = {self.sequence}')
#             self.client.send_goal(self.goal_list[self.sequence])
#         else:
#             print(f'2-client_state={self.client.get_state()},GoalStatus.ACTIVE={GoalStatus.ACTIVE}, sequence = {self.sequence}')
#             if (self.sequence == self.num_goals - 1):  # 마지막 목표에 도달하면
#                 self.stop()
            

                
#     def stop(self):
#         self.client.cancel_all_goals()
#         rospy.signal_shutdown("all goals completed")

# def main():
#     rospy.init_node('navigation_client')
#     nc = NavigationClient()
#     rate = rospy.Rate(0.5)
    
#     while not rospy.is_shutdown():
#         nc.run()
#         rate.sleep()
    
 
# if __name__ == '__main__':
#     main()
    
    





    
    
    
