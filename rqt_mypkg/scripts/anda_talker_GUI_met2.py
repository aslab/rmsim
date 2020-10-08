#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from math import pi
from PyQt5.QtCore import *
import threading


class anda_talker2(QObject):

    flag = False
    wait_for_input = pyqtSignal()
    done = pyqtSignal()

    pub1 = [
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
    # Para fallo bias
    pub2 = [
        # Pata r1
        [rospy.Publisher('/robominer/Rev3_r_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_1_biased_position_controller/command', Float64,
                         queue_size=10)],
        # Pata r2
        [rospy.Publisher('/robominer/Rev3_r_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_2_biased_position_controller/command', Float64,
                         queue_size=10)],
        # Pata r3
        [rospy.Publisher('/robominer/Rev3_r_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_r_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_r_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_r_3_biased_position_controller/command', Float64,
                         queue_size=10)],
        # Pata l1
        [rospy.Publisher('/robominer/Rev3_l_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_1_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_1_biased_position_controller/command', Float64,
                         queue_size=10)],
        # Pata l2
        [rospy.Publisher('/robominer/Rev3_l_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_2_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_2_biased_position_controller/command', Float64,
                         queue_size=10)],
        # Pata l3
        [rospy.Publisher('/robominer/Rev3_l_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev5_l_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev8_l_3_biased_position_controller/command', Float64, queue_size=10),
         rospy.Publisher('/robominer/Rev11_l_3_biased_position_controller/command', Float64,
                         queue_size=10)],

    ]

    # rospy.init_node('robominer_anda_talker', anonymous=False)
    #rate = rospy.Rate(10)  # 10hz

    def worker(self,num):
        #global flag
        #global done
        """función que realiza el trabajo en el hilo"""
        #print('Hilo', num, 'iniciado')
        flag2 = False  # en la primera iteración la pata solo avanza medio rango
        n = 10  # número de intervalos en que partimos cada movimiento
        while not rospy.is_shutdown():

            if not self.flag:
                # Pata arriba
                for i in range(n):
                    self.pos[num][1] = self.pos[num][1] - pi / (12 * n)
                    self.pos[num][2] = self.pos[num][2] + pi / (12 * n)
                    self.pub1[num][1].publish(self.pos[num][1])
                    self.pub1[num][2].publish(self.pos[num][2])
                    #Para fallo bias
                    self.pub2[num][1].publish(self.pos[num][1])
                    self.pub2[num][2].publish(self.pos[num][2])
                    # rospy.sleep(0.5)
                    # rate.sleep()

                # Pata adelante
                for i in range(n):
                    if not flag2:
                        if num < 4:
                            self.pos[num][0] = self.pos[num][0] + pi / (12 * n)
                        else:
                            self.pos[num][0] = self.pos[num][0] - pi / (12 * n)
                    else:
                        if num < 4:
                            self.pos[num][0] = self.pos[num][0] + pi / (6 * n)
                        else:
                            self.pos[num][0] = self.pos[num][0] - pi / (6 * n)

                    self.pub1[num][0].publish(self.pos[num][0])
                    #Para fallo bias
                    self.pub2[num][0].publish(self.pos[num][0])
                    # rate.sleep()

                rospy.sleep(0.5)

                # Pata abajo
                for i in range(n):
                    self.pos[num][1] = self.pos[num][1] + pi / (12 * n)
                    self.pos[num][2] = self.pos[num][2] - pi / (12 * n)
                    self.pub1[num][1].publish(self.pos[num][1])
                    self.pub1[num][2].publish(self.pos[num][2])
                    #Para fallo bias
                    self.pub2[num][1].publish(self.pos[num][1])
                    self.pub2[num][2].publish(self.pos[num][2])
                    # rate.sleep()

                rospy.sleep(0.5)

                # Pata atrás
                for i in range(n):
                    if num < 4:
                        self.pos[num][0] = self.pos[num][0] - pi / (6 * n)
                    else:
                        self.pos[num][0] = self.pos[num][0] + pi / (6 * n)

                    self.pub1[num][0].publish(self.pos[num][0])
                    #Para fallo bias
                    self.pub2[num][0].publish(self.pos[num][0])
                    # rate.sleep()

                rospy.sleep(1)

                flag2 = True

            else:
                break

        #print('Hilo', num, 'parado')

        return

    @pyqtSlot()
    def talker(self):
        self.wait_for_input.emit()
        #print('En talker flag = ', self.flag)

        self.pos = [
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

        t_r1 = threading.Thread(target=self.worker, args=(0,), name='Hilo pata r1')
        t_r2 = threading.Thread(target=self.worker, args=(1,), name='Hilo pata r2')
        t_r3 = threading.Thread(target=self.worker, args=(2,), name='Hilo pata r3')
        t_l1 = threading.Thread(target=self.worker, args=(3,), name='Hilo pata l1')
        t_l2 = threading.Thread(target=self.worker, args=(4,), name='Hilo pata l2')
        t_l3 = threading.Thread(target=self.worker, args=(5,), name='Hilo pata l3')

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


        t_r1.join()
        t_l2.join()
        t_r3.join()
        t_l1.join()
        t_r2.join()
        t_l3.join()

        self.done.emit()
        self.flag = False

    def run(self):
        pass