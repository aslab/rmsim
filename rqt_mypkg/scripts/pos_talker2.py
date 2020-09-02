#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from PyQt5.QtCore import *
from math import pi


class set_pos(QObject):

    def talker2(self, pata, art, ang):

        ang_rad = ang*pi/180
        if pata == 'Pata r1':
            if art == 'Rev3':
                i = 0
                j = 0
            if art == 'Rev5':
                i = 0
                j = 1
            if art == 'Rev8':
                i = 0
                j = 2
            if art == 'Rev11':
                i = 0
                j = 3
        if pata == 'Pata r2':
            if art == 'Rev3':
                i = 1
                j = 0
            if art == 'Rev5':
                i = 1
                j = 1
            if art == 'Rev8':
                i = 1
                j = 2
            if art == 'Rev11':
                i = 1
                j = 3
        if pata == 'Pata r3':
            if art == 'Rev3':
                i = 2
                j = 0
            if art == 'Rev5':
                i = 2
                j = 1
            if art == 'Rev8':
                i = 2
                j = 2
            if art == 'Rev11':
                i = 2
                j = 3
        if pata == 'Pata l1':
            if art == 'Rev3':
                i = 3
                j = 0
            if art == 'Rev5':
                i = 3
                j = 1
            if art == 'Rev8':
                i = 3
                j = 2
            if art == 'Rev11':
                i = 3
                j = 3
        if pata == 'Pata l2':
            if art == 'Rev3':
                i = 4
                j = 0
            if art == 'Rev5':
                i = 4
                j = 1
            if art == 'Rev8':
                i = 4
                j = 2
            if art == 'Rev11':
                i = 4
                j = 3
        if pata == 'Pata l3':
            if art == 'Rev3':
                i = 5
                j = 0
            if art == 'Rev5':
                i = 5
                j = 1
            if art == 'Rev8':
                i = 5
                j = 2
            if art == 'Rev11':
                i = 5
                j = 3


        pub1 =[
                #Pata r1
            [rospy.Publisher('/robominer/Rev3_r_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_1_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_1_position_controller/command', Float64, queue_size=10)],
                #Pata r2
            [rospy.Publisher('/robominer/Rev3_r_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_2_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_2_position_controller/command', Float64, queue_size=10)],
                #Pata r3
            [rospy.Publisher('/robominer/Rev3_r_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_3_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_3_position_controller/command', Float64, queue_size=10)],
                #Pata l1
            [rospy.Publisher('/robominer/Rev3_l_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_1_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_1_position_controller/command', Float64, queue_size=10)],
                #Pata l2
            [rospy.Publisher('/robominer/Rev3_l_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_2_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_2_position_controller/command', Float64, queue_size=10)],
                #Pata l3
            [rospy.Publisher('/robominer/Rev3_l_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_3_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_3_position_controller/command', Float64, queue_size=10)],
        ]

        pub2 = [
            # Pata r1
            [rospy.Publisher('/robominer/Rev3_r_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_1_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_r_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_1_biased_position_controller/command', Float64, queue_size=10)],
            # Pata r2
            [rospy.Publisher('/robominer/Rev3_r_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_2_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_r_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_2_biased_position_controller/command', Float64, queue_size=10)],
            # Pata r3
            [rospy.Publisher('/robominer/Rev3_r_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_3_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_r_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_3_biased_position_controller/command', Float64, queue_size=10)],
            # Pata l1
            [rospy.Publisher('/robominer/Rev3_l_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_1_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_l_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_1_biased_position_controller/command', Float64, queue_size=10)],
            # Pata l2
            [rospy.Publisher('/robominer/Rev3_l_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_2_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_l_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_2_biased_position_controller/command', Float64, queue_size=10)],
            # Pata l3
            [rospy.Publisher('/robominer/Rev3_l_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_3_biased_position_controller/command', Float64, queue_size=10),
             rospy.Publisher('/robominer/Rev8_l_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_3_biased_position_controller/command', Float64, queue_size=10)],
        ]

        #rospy.init_node('robominer_joint_command_talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():

            for x in range(10):

                rospy.loginfo(ang_rad)

                pub1[i][j].publish(ang_rad)
                pub2[i][j].publish(ang_rad)

                rate.sleep()

            break

    def run(self):
        pass