#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from math import pi


def talker():
    pub = [
        # Pata r1
        [rospy.Publisher('/robominer/Rev3_r_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_1_position_controller/command', Float64, queue_size=10)],
        # Pata r2
        [rospy.Publisher('/robominer/Rev3_r_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_2_position_controller/command', Float64, queue_size=10)],
        # Pata r3
        [rospy.Publisher('/robominer/Rev3_r_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_3_position_controller/command', Float64, queue_size=10)],
        # Pata l1
        [rospy.Publisher('/robominer/Rev3_l_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_1_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_1_position_controller/command', Float64, queue_size=10)],
        # Pata l2
        [rospy.Publisher('/robominer/Rev3_l_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_2_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_2_position_controller/command', Float64, queue_size=10)],
        # Pata l3
        [rospy.Publisher('/robominer/Rev3_l_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_3_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_3_position_controller/command', Float64, queue_size=10)],

    ]

    rospy.init_node('robominer_anda_talker', anonymous=False)
    # rospy.init_node('robominer_joint_command_talker', anonymous=False)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
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

        #Adelante pata r1
        #Sube
        pos[0][1] = pos[0][1] - pi/8
        pos[0][2] = pos[0][2] + pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[0][1].publish(pos[0][1])
        pub[0][2].publish(pos[0][2])
        rate.sleep()
        #Avanza
        pos[0][0] = pos[0][0] + pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[0][0].publish(pos[0][0])
        rate.sleep()
        #Baja
        pos[0][1] = pos[0][1] + pi/8
        pos[0][2] = pos[0][2] - pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[0][1].publish(pos[0][1])
        pub[0][2].publish(pos[0][2])
        rate.sleep()

        #Adelante pata l2
        #Sube
        pos[4][1] = pos[4][1] - pi/8
        pos[4][2] = pos[4][2] + pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[4][1].publish(pos[4][1])
        pub[4][2].publish(pos[4][2])
        rate.sleep()
        #Avanza
        pos[4][0] = pos[4][0] - pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[4][0].publish(pos[4][0])
        rate.sleep()
        #Baja
        pos[4][1] = pos[4][1] + pi/8
        pos[4][2] = pos[4][2] - pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[4][1].publish(pos[4][1])
        pub[4][2].publish(pos[4][2])
        rate.sleep()

        #Adelante pata r3
        #Sube
        pos[2][1] = pos[2][1] - pi/8
        pos[2][2] = pos[2][2] + pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[2][1].publish(pos[2][1])
        pub[2][2].publish(pos[2][2])
        rate.sleep()
        #Avanza
        pos[2][0] = pos[2][0] + pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[2][0].publish(pos[2][0])
        rate.sleep()
        #Baja
        pos[2][1] = pos[2][1] + pi/8
        pos[2][2] = pos[2][2] - pi/8
        #for x in range(3):
        #rospy.loginfo(pos)
        pub[2][1].publish(pos[2][1])
        pub[2][2].publish(pos[2][2])
        rate.sleep()

        break


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass