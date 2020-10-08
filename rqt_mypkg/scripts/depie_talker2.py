#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from math import pi
from PyQt5.QtCore import *


class depie_talker(QObject):

    wait_for_input = pyqtSignal()
    done = pyqtSignal()

    @pyqtSlot()
    def talker(self):
        self.wait_for_input.emit()
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

        pub2 =[
                #Pata r1
            [rospy.Publisher('/robominer/Rev3_r_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_1_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_1_biased_position_controller/command', Float64, queue_size=10)],
                #Pata r2
            [rospy.Publisher('/robominer/Rev3_r_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_2_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_2_biased_position_controller/command', Float64, queue_size=10)],
                #Pata r3
            [rospy.Publisher('/robominer/Rev3_r_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_3_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_r_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_3_biased_position_controller/command', Float64, queue_size=10)],
                #Pata l1
            [rospy.Publisher('/robominer/Rev3_l_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_1_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_1_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_1_biased_position_controller/command', Float64, queue_size=10)],
                #Pata l2
            [rospy.Publisher('/robominer/Rev3_l_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_2_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_2_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_2_biased_position_controller/command', Float64, queue_size=10)],
                #Pata l3
            [rospy.Publisher('/robominer/Rev3_l_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_3_biased_position_controller/command', Float64, queue_size=10),
            rospy.Publisher('/robominer/Rev8_l_3_biased_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_3_biased_position_controller/command', Float64, queue_size=10)],

        ]

        #rospy.init_node('robominer_joint_command_talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():

            pos = [
                # Pata r1
                [pi / 4, -pi / 4, pi / 2, pi / 4],
                # Pata r2
                [0, -pi / 4, pi / 2, pi / 4],
                # Pata r3
                [-pi / 4, -pi / 4, pi / 2, pi / 4],
                # Pata l1
                [-pi / 4, -pi / 4, pi / 2, pi / 4],
                # Pata l2
                [0, -pi / 4, pi / 2, pi / 4],
                # Pata l3
                [pi / 4, -pi / 4, pi / 2, pi / 4]
            ]

            for x in range(10):

                #rospy.loginfo(pos)
                # Pata r1
                pub1[0][0].publish(pos[0][0])
                pub1[0][1].publish(pos[0][1])
                pub1[0][2].publish(pos[0][2])
                pub1[0][3].publish(pos[0][3])
                # Pata r2
                pub1[1][0].publish(pos[1][0])
                pub1[1][1].publish(pos[1][1])
                pub1[1][2].publish(pos[1][2])
                pub1[1][3].publish(pos[1][3])
                # Pata r3
                pub1[2][0].publish(pos[2][0])
                pub1[2][1].publish(pos[2][1])
                pub1[2][2].publish(pos[2][2])
                pub1[2][3].publish(pos[2][3])
                # Pata l1
                pub1[3][0].publish(pos[3][0])
                pub1[3][1].publish(pos[3][1])
                pub1[3][2].publish(pos[3][2])
                pub1[3][3].publish(pos[3][3])
                # Pata l2
                pub1[4][0].publish(pos[4][0])
                pub1[4][1].publish(pos[4][1])
                pub1[4][2].publish(pos[4][2])
                pub1[4][3].publish(pos[4][3])
                # Pata l3
                pub1[5][0].publish(pos[5][0])
                pub1[5][1].publish(pos[5][1])
                pub1[5][2].publish(pos[5][2])
                pub1[5][3].publish(pos[5][3])

                # Fallo bias
                # Pata r1
                pub2[0][0].publish(pos[0][0])
                pub2[0][1].publish(pos[0][1])
                pub2[0][2].publish(pos[0][2])
                pub2[0][3].publish(pos[0][3])
                # Pata r2
                pub2[1][0].publish(pos[1][0])
                pub2[1][1].publish(pos[1][1])
                pub2[1][2].publish(pos[1][2])
                pub2[1][3].publish(pos[1][3])
                # Pata r3
                pub2[2][0].publish(pos[2][0])
                pub2[2][1].publish(pos[2][1])
                pub2[2][2].publish(pos[2][2])
                pub2[2][3].publish(pos[2][3])
                # Pata l1
                pub2[3][0].publish(pos[3][0])
                pub2[3][1].publish(pos[3][1])
                pub2[3][2].publish(pos[3][2])
                pub2[3][3].publish(pos[3][3])
                # Pata l2
                pub2[4][0].publish(pos[4][0])
                pub2[4][1].publish(pos[4][1])
                pub2[4][2].publish(pos[4][2])
                pub2[4][3].publish(pos[4][3])
                # Pata l3
                pub2[5][0].publish(pos[5][0])
                pub2[5][1].publish(pos[5][1])
                pub2[5][2].publish(pos[5][2])
                pub2[5][3].publish(pos[5][3])

                rate.sleep()

            pos = [
                # Pata r1
                [pi / 4, 0, pi / 2, 0],
                # Pata r2
                [0, 0, pi / 2, 0],
                # Pata r3
                [-pi / 4, 0, pi / 2, 0],
                # Pata l1
                [-pi / 4, 0, pi / 2, 0],
                # Pata l2
                [0, 0, pi / 2, 0],
                # Pata l3
                [pi / 4, 0, pi / 2, 0]
            ]

            for x in range(10):

                #rospy.loginfo(pos)
                # Pata r1
                pub1[0][0].publish(pos[0][0])
                pub1[0][1].publish(pos[0][1])
                pub1[0][2].publish(pos[0][2])
                pub1[0][3].publish(pos[0][3])
                # Pata r2
                pub1[1][0].publish(pos[1][0])
                pub1[1][1].publish(pos[1][1])
                pub1[1][2].publish(pos[1][2])
                pub1[1][3].publish(pos[1][3])
                # Pata r3
                pub1[2][0].publish(pos[2][0])
                pub1[2][1].publish(pos[2][1])
                pub1[2][2].publish(pos[2][2])
                pub1[2][3].publish(pos[2][3])
                # Pata l1
                pub1[3][0].publish(pos[3][0])
                pub1[3][1].publish(pos[3][1])
                pub1[3][2].publish(pos[3][2])
                pub1[3][3].publish(pos[3][3])
                # Pata l2
                pub1[4][0].publish(pos[4][0])
                pub1[4][1].publish(pos[4][1])
                pub1[4][2].publish(pos[4][2])
                pub1[4][3].publish(pos[4][3])
                # Pata l3
                pub1[5][0].publish(pos[5][0])
                pub1[5][1].publish(pos[5][1])
                pub1[5][2].publish(pos[5][2])
                pub1[5][3].publish(pos[5][3])

                # Fallo bias
                # Pata r1
                pub2[0][0].publish(pos[0][0])
                pub2[0][1].publish(pos[0][1])
                pub2[0][2].publish(pos[0][2])
                pub2[0][3].publish(pos[0][3])
                # Pata r2
                pub2[1][0].publish(pos[1][0])
                pub2[1][1].publish(pos[1][1])
                pub2[1][2].publish(pos[1][2])
                pub2[1][3].publish(pos[1][3])
                # Pata r3
                pub2[2][0].publish(pos[2][0])
                pub2[2][1].publish(pos[2][1])
                pub2[2][2].publish(pos[2][2])
                pub2[2][3].publish(pos[2][3])
                # Pata l1
                pub2[3][0].publish(pos[3][0])
                pub2[3][1].publish(pos[3][1])
                pub2[3][2].publish(pos[3][2])
                pub2[3][3].publish(pos[3][3])
                # Pata l2
                pub2[4][0].publish(pos[4][0])
                pub2[4][1].publish(pos[4][1])
                pub2[4][2].publish(pos[4][2])
                pub2[4][3].publish(pos[4][3])
                # Pata l3
                pub2[5][0].publish(pos[5][0])
                pub2[5][1].publish(pos[5][1])
                pub2[5][2].publish(pos[5][2])
                pub2[5][3].publish(pos[5][3])
                rate.sleep()

            pos = [
                # Pata r1
                [pi / 4, pi / 4, pi / 4, 0],
                # Pata r2
                [0, pi / 4, pi / 4, 0],
                # Pata r3
                [-pi / 4, pi / 4, pi / 4, 0],
                # Pata l1
                [-pi / 4, pi / 4, pi / 4, 0],
                # Pata l2
                [0, pi / 4, pi / 4, 0],
                # Pata l3
                [pi / 4, pi / 4, pi / 4, 0]
            ]

            for x in range(10):

                #rospy.loginfo(pos)
                # Pata r1
                pub1[0][0].publish(pos[0][0])
                pub1[0][1].publish(pos[0][1])
                pub1[0][2].publish(pos[0][2])
                pub1[0][3].publish(pos[0][3])
                # Pata r2
                pub1[1][0].publish(pos[1][0])
                pub1[1][1].publish(pos[1][1])
                pub1[1][2].publish(pos[1][2])
                pub1[1][3].publish(pos[1][3])
                # Pata r3
                pub1[2][0].publish(pos[2][0])
                pub1[2][1].publish(pos[2][1])
                pub1[2][2].publish(pos[2][2])
                pub1[2][3].publish(pos[2][3])
                # Pata l1
                pub1[3][0].publish(pos[3][0])
                pub1[3][1].publish(pos[3][1])
                pub1[3][2].publish(pos[3][2])
                pub1[3][3].publish(pos[3][3])
                # Pata l2
                pub1[4][0].publish(pos[4][0])
                pub1[4][1].publish(pos[4][1])
                pub1[4][2].publish(pos[4][2])
                pub1[4][3].publish(pos[4][3])
                # Pata l3
                pub1[5][0].publish(pos[5][0])
                pub1[5][1].publish(pos[5][1])
                pub1[5][2].publish(pos[5][2])
                pub1[5][3].publish(pos[5][3])

                # Fallo bias
                # Pata r1
                pub2[0][0].publish(pos[0][0])
                pub2[0][1].publish(pos[0][1])
                pub2[0][2].publish(pos[0][2])
                pub2[0][3].publish(pos[0][3])
                # Pata r2
                pub2[1][0].publish(pos[1][0])
                pub2[1][1].publish(pos[1][1])
                pub2[1][2].publish(pos[1][2])
                pub2[1][3].publish(pos[1][3])
                # Pata r3
                pub2[2][0].publish(pos[2][0])
                pub2[2][1].publish(pos[2][1])
                pub2[2][2].publish(pos[2][2])
                pub2[2][3].publish(pos[2][3])
                # Pata l1
                pub2[3][0].publish(pos[3][0])
                pub2[3][1].publish(pos[3][1])
                pub2[3][2].publish(pos[3][2])
                pub2[3][3].publish(pos[3][3])
                # Pata l2
                pub2[4][0].publish(pos[4][0])
                pub2[4][1].publish(pos[4][1])
                pub2[4][2].publish(pos[4][2])
                pub2[4][3].publish(pos[4][3])
                # Pata l3
                pub2[5][0].publish(pos[5][0])
                pub2[5][1].publish(pos[5][1])
                pub2[5][2].publish(pos[5][2])
                pub2[5][3].publish(pos[5][3])

                rate.sleep()

            break

        self.done.emit()

    def run(self):
        pass
