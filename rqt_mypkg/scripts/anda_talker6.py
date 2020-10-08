#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from math import pi
import threading
import numpy as np

def worker(num):
    """función que realiza el trabajo en el hilo"""
    print('Hilo', num, 'iniciado')
    flag = False #en la primera iteración la pata solo avanza medio rango

    while not rospy.is_shutdown():
        # Pata arriba
        pos[num][1] = pos[num][1] - pi / 16
        pos[num][2] = pos[num][2] + pi / 16
        pub[num][1].publish(pos[num][1])
        pub[num][2].publish(pos[num][2])
        #rospy.sleep(0.5)

        #Pata adelante
        if not flag:
            if num < 4:
                pos[num][0] = pos[num][0] + pi / 16
            else:
                pos[num][0] = pos[num][0] - pi / 16
        else:
            if num < 4:
                pos[num][0] = pos[num][0] + pi / 8
            else:
                pos[num][0] = pos[num][0] - pi / 8

        pub[num][0].publish(pos[num][0])
        rospy.sleep(0.5)
        #rate.sleep()

        #Pata abajo
        pos[num][1] = pos[num][1] + pi / 16
        pos[num][2] = pos[num][2] - pi / 16
        pub[num][1].publish(pos[num][1])
        pub[num][2].publish(pos[num][2])
        rospy.sleep(0.5)
        #rate.sleep()

        #Pata atrás
        if num < 4:
            pos[num][0] = pos[num][0] - pi / 8
        else:
            pos[num][0] = pos[num][0] + pi / 8

        pub[num][0].publish(pos[num][0])
        rospy.sleep(1)
        #rate.sleep()
        #rate.sleep()

        flag = True

    return


if __name__ == '__main__':
    try:

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
        rate = rospy.Rate(2)  # 2hz

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
        '''
        threads = list()

        for i in range(6):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
        '''
        t_r1 = threading.Thread(target=worker, args=(0,), name='Hilo pata r1')
        t_r2 = threading.Thread(target=worker, args=(1,), name='Hilo pata r2')
        t_r3 = threading.Thread(target=worker, args=(2,), name='Hilo pata r3')
        t_l1 = threading.Thread(target=worker, args=(3,), name='Hilo pata l1')
        t_l2 = threading.Thread(target=worker, args=(4,), name='Hilo pata l2')
        t_l3 = threading.Thread(target=worker, args=(5,), name='Hilo pata l3')

        t_r1.start()
        rospy.sleep(0.25)
        t_l2.start()
        rospy.sleep(0.25)
        t_r3.start()
        rospy.sleep(0.5)
        t_l1.start()
        rospy.sleep(0.25)
        t_r2.start()
        rospy.sleep(0.25)
        t_l3.start()
        '''

        t_r1.start()
        rospy.sleep(0.05)
        t_l1.start()
        rospy.sleep(0.25)
        t_r2.start()
        rospy.sleep(0.05)
        t_l2.start()
        rospy.sleep(0.25)
        t_r3.start()
        rospy.sleep(0.05)
        t_l3.start()
        '''

    except rospy.ROSInterruptException:
        pass