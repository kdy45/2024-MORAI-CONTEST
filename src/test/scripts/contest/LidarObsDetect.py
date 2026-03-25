#! /usr/bin/env python3

# -*- coding : utf-8 -*-

import rospy
import os
from sensor_msgs.msg import LaserScan
from smarp_msgs.msg import objectStatus, objInfo, lidarStatus

class weBotLidarTest :
    def __init__(self) :
        rospy.init_node("LidarObsDetect")
        rospy.Subscriber("/scan", LaserScan, self.lidar_CB)
        rospy.Subscriber("/lidar_range", lidarStatus, self.lidar_stat_CB)
        self.obj_pub = rospy.Publisher("/obj_scan", objectStatus, queue_size = 1)
        self.objects_pub = objectStatus()
        self.lidar_range = [150,190]
        self.lidar_dist = 0.85

    def lidar_stat_CB(self, msg) :
        self.lidar_range = msg.range
        self.lidar_dist = msg.dist  

    def lidar_CB(self, msg) :
        # os.system("clear")
        self.scan_msg = msg

        obstacles = self.filtering(self.lidar_range[0], self.lidar_range[-1], self.lidar_dist)
        self.objects_pub = self.grouping(obstacles, 0.1)

        self.obj_pub.publish(self.objects_pub)

    def filtering(self, rightAngle, leftAngle, distance) :
        obstacles = []
        for index, value in enumerate(self.scan_msg.ranges) :
            if ( rightAngle <= index <= leftAngle ) and value < distance :
                # print(f"[{index},{value}]")
                obstacles.append([index, value])

        return obstacles

    def grouping(self, obstacles, size_limit) :
        no_group = 0
        pre_obj_deg = 0                 # deg of previous point
        pre_obj_dist = 0                # dist of previous point
        one_grp = objInfo()             # deg=[ ], dist=[ ]
        obs_info = objectStatus()           # [one_Group, two_Group, ...]
        
        for idx, [deg, dist]  in enumerate(obstacles) :
            # print(f'obs=[{idx}] {deg} - {dist}')

            if (pre_obj_deg == 0) :                                                # 첫번째 Obj 정보 처리
                one_grp.deg.append(deg)
                one_grp.dist.append(dist)
                pre_obj_deg = deg
                pre_obj_dist = dist
                no_group += 1
            elif (idx == len(obstacles) - 1) :                                      # 마지막 Obj 정보 처리
                one_grp.deg.append(deg)
                one_grp.dist.append(dist)
                obs_info.objects.append(one_grp)
                # one_grp = []

            elif (deg - pre_obj_deg) > 1 or abs(pre_obj_dist - dist) > size_limit :    # 다른 물체인 경우 --> 이전 물체 등록, 새 물체 생성

                # print(f'deg={deg}, pre_obj_deg={pre_obj_deg}, deg - pre_obj_deg={deg - pre_obj_deg},abs(pre_obj_dist-dist)={abs(pre_obj_dist - dist)}')
                
                one_grp.deg.append(pre_obj_deg)
                one_grp.dist.append(pre_obj_dist)                
                obs_info.objects.append(one_grp)
                one_grp = objInfo()
                pre_obj_deg = deg
                pre_obj_dist = dist
                no_group += 1
                one_grp.deg.append(deg)
                one_grp.dist.append(dist)
            else :
                # one_grp.deg.append(deg)
                # one_grp.dist.append(dist)
                pre_obj_deg = deg
                pre_obj_dist = dist

        obs_info.no_objects = no_group

        print(f'{obs_info}')

        return obs_info        

if __name__ == '__main__' :
    try :
        wb = weBotLidarTest()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    

    
