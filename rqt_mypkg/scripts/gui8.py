#!/usr/bin/env python3

import sys
from gui8_ui import *
import rospy
from pos_listener import *
from vel_listener import *
from par_listener import *
from PyQt5.QtCore import *
from depie_talker2 import *
from pos_talker2 import *
from anda_talker_GUI_met1 import *
from anda_talker_GUI_met2 import *
import dynamic_reconfigure.client
from robominer_plugins.srv import robominer_srv
from controller_manager_msgs.srv import SwitchController
import numpy as np
import datetime

rospy.init_node('robominer_GUI', anonymous=False)

# Fallos a y b (actuador muerto y actuador con fuerza reducida, respectivamente)
params_a = {'p': 0, 'i': 0, 'd': 0}
params_b1 = {'p': 50, 'i': 0.01, 'd': 1} #articulaciones 5 y 8
params_b2 = {'p': 10, 'i': 0.01, 'd': 1} #articulaciones 3 y 11
client_Rev3_r_1 = dynamic_reconfigure.client.Client("/robominer/Rev3_r_1_position_controller/pid")
client_Rev3_r_2 = dynamic_reconfigure.client.Client("/robominer/Rev3_r_2_position_controller/pid")
client_Rev3_r_3 = dynamic_reconfigure.client.Client("/robominer/Rev3_r_3_position_controller/pid")
client_Rev3_l_1 = dynamic_reconfigure.client.Client("/robominer/Rev3_l_1_position_controller/pid")
client_Rev3_l_2 = dynamic_reconfigure.client.Client("/robominer/Rev3_l_2_position_controller/pid")
client_Rev3_l_3 = dynamic_reconfigure.client.Client("/robominer/Rev3_l_3_position_controller/pid")
client_Rev5_r_1 = dynamic_reconfigure.client.Client("/robominer/Rev5_r_1_position_controller/pid")
client_Rev5_r_2 = dynamic_reconfigure.client.Client("/robominer/Rev5_r_2_position_controller/pid")
client_Rev5_r_3 = dynamic_reconfigure.client.Client("/robominer/Rev5_r_3_position_controller/pid")
client_Rev5_l_1 = dynamic_reconfigure.client.Client("/robominer/Rev5_l_1_position_controller/pid")
client_Rev5_l_2 = dynamic_reconfigure.client.Client("/robominer/Rev5_l_2_position_controller/pid")
client_Rev5_l_3 = dynamic_reconfigure.client.Client("/robominer/Rev5_l_3_position_controller/pid")
client_Rev8_r_1 = dynamic_reconfigure.client.Client("/robominer/Rev8_r_1_position_controller/pid")
client_Rev8_r_2 = dynamic_reconfigure.client.Client("/robominer/Rev8_r_2_position_controller/pid")
client_Rev8_r_3 = dynamic_reconfigure.client.Client("/robominer/Rev8_r_3_position_controller/pid")
client_Rev8_l_1 = dynamic_reconfigure.client.Client("/robominer/Rev8_l_1_position_controller/pid")
client_Rev8_l_2 = dynamic_reconfigure.client.Client("/robominer/Rev8_l_2_position_controller/pid")
client_Rev8_l_3 = dynamic_reconfigure.client.Client("/robominer/Rev8_l_3_position_controller/pid")
client_Rev11_r_1 = dynamic_reconfigure.client.Client("/robominer/Rev11_r_1_position_controller/pid")
client_Rev11_r_2 = dynamic_reconfigure.client.Client("/robominer/Rev11_r_2_position_controller/pid")
client_Rev11_r_3 = dynamic_reconfigure.client.Client("/robominer/Rev11_r_3_position_controller/pid")
client_Rev11_l_1 = dynamic_reconfigure.client.Client("/robominer/Rev11_l_1_position_controller/pid")
client_Rev11_l_2 = dynamic_reconfigure.client.Client("/robominer/Rev11_l_2_position_controller/pid")
client_Rev11_l_3 = dynamic_reconfigure.client.Client("/robominer/Rev11_l_3_position_controller/pid")
#Para los controladores desviados
client_Rev3_r_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_r_1_biased_position_controller/pid")
client_Rev3_r_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_r_2_biased_position_controller/pid")
client_Rev3_r_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_r_3_biased_position_controller/pid")
client_Rev3_l_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_l_1_biased_position_controller/pid")
client_Rev3_l_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_l_2_biased_position_controller/pid")
client_Rev3_l_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev3_l_3_biased_position_controller/pid")
client_Rev5_r_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_r_1_biased_position_controller/pid")
client_Rev5_r_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_r_2_biased_position_controller/pid")
client_Rev5_r_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_r_3_biased_position_controller/pid")
client_Rev5_l_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_l_1_biased_position_controller/pid")
client_Rev5_l_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_l_2_biased_position_controller/pid")
client_Rev5_l_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev5_l_3_biased_position_controller/pid")
client_Rev8_r_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_r_1_biased_position_controller/pid")
client_Rev8_r_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_r_2_biased_position_controller/pid")
client_Rev8_r_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_r_3_biased_position_controller/pid")
client_Rev8_l_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_l_1_biased_position_controller/pid")
client_Rev8_l_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_l_2_biased_position_controller/pid")
client_Rev8_l_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev8_l_3_biased_position_controller/pid")
client_Rev11_r_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_r_1_biased_position_controller/pid")
client_Rev11_r_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_r_2_biased_position_controller/pid")
client_Rev11_r_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_r_3_biased_position_controller/pid")
client_Rev11_l_1_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_l_1_biased_position_controller/pid")
client_Rev11_l_2_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_l_2_biased_position_controller/pid")
client_Rev11_l_3_biased = dynamic_reconfigure.client.Client("/robominer/Rev11_l_3_biased_position_controller/pid")

#Canal predeterminado
canal = 'Ángulo'

#Fallos sensores
sensor_flags = np.zeros(24)
fallo_sens = False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    msg = pyqtSignal(str, str, int)


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setupThreads()
        self.pos = pos_listener()
        self.pos.msg.connect(self.updateLCD)
        self.pos.start()
        self.vel = vel_listener()
        self.vel.start()
        self.par = par_listener()
        self.par.start()
        self.comboBox_canal.setCurrentText("Seleccione canal")
        self.comboBox_canal.activated[str].connect(self.set_canal)
        self.comboBox_met.activated[str].connect(self.set_alg)
        self.comboBox_art.activated[str].connect(self.show_lim)
        self.comboBox_fallos.activated[str].connect(self.show_fallo)
        self.lineEdit_rev3_r1.returnPressed.connect(self.send_to_rev3_r1)
        self.lineEdit_rev3_r1.setMaxLength(4)
        self.lineEdit_rev3_r2.returnPressed.connect(self.send_to_rev3_r2)
        self.lineEdit_rev3_r2.setMaxLength(4)
        self.lineEdit_rev3_r3.returnPressed.connect(self.send_to_rev3_r3)
        self.lineEdit_rev3_r3.setMaxLength(4)
        self.lineEdit_rev3_l1.returnPressed.connect(self.send_to_rev3_l1)
        self.lineEdit_rev3_l1.setMaxLength(4)
        self.lineEdit_rev3_l2.returnPressed.connect(self.send_to_rev3_l2)
        self.lineEdit_rev3_l2.setMaxLength(4)
        self.lineEdit_rev3_l3.returnPressed.connect(self.send_to_rev3_l3)
        self.lineEdit_rev3_l3.setMaxLength(4)
        self.lineEdit_rev5_r1.returnPressed.connect(self.send_to_rev5_r1)
        self.lineEdit_rev5_r1.setMaxLength(4)
        self.lineEdit_rev5_r2.returnPressed.connect(self.send_to_rev5_r2)
        self.lineEdit_rev5_r2.setMaxLength(4)
        self.lineEdit_rev5_r3.returnPressed.connect(self.send_to_rev5_r3)
        self.lineEdit_rev5_r3.setMaxLength(4)
        self.lineEdit_rev5_l1.returnPressed.connect(self.send_to_rev5_l1)
        self.lineEdit_rev5_l1.setMaxLength(4)
        self.lineEdit_rev5_l2.returnPressed.connect(self.send_to_rev5_l2)
        self.lineEdit_rev5_l2.setMaxLength(4)
        self.lineEdit_rev5_l3.returnPressed.connect(self.send_to_rev5_l3)
        self.lineEdit_rev5_l3.setMaxLength(4)
        self.lineEdit_rev8_r1.returnPressed.connect(self.send_to_rev8_r1)
        self.lineEdit_rev8_r1.setMaxLength(4)
        self.lineEdit_rev8_r2.returnPressed.connect(self.send_to_rev8_r2)
        self.lineEdit_rev8_r2.setMaxLength(4)
        self.lineEdit_rev8_r3.returnPressed.connect(self.send_to_rev8_r3)
        self.lineEdit_rev8_r3.setMaxLength(4)
        self.lineEdit_rev8_l1.returnPressed.connect(self.send_to_rev8_l1)
        self.lineEdit_rev8_l1.setMaxLength(4)
        self.lineEdit_rev8_l2.returnPressed.connect(self.send_to_rev8_l2)
        self.lineEdit_rev8_l2.setMaxLength(4)
        self.lineEdit_rev8_l3.returnPressed.connect(self.send_to_rev8_l3)
        self.lineEdit_rev8_l3.setMaxLength(4)
        self.lineEdit_rev11_r1.returnPressed.connect(self.send_to_rev11_r1)
        self.lineEdit_rev11_r1.setMaxLength(4)
        self.lineEdit_rev11_r2.returnPressed.connect(self.send_to_rev11_r2)
        self.lineEdit_rev11_r2.setMaxLength(4)
        self.lineEdit_rev11_r3.returnPressed.connect(self.send_to_rev11_r3)
        self.lineEdit_rev11_r3.setMaxLength(4)
        self.lineEdit_rev11_l1.returnPressed.connect(self.send_to_rev11_l1)
        self.lineEdit_rev11_l1.setMaxLength(4)
        self.lineEdit_rev11_l2.returnPressed.connect(self.send_to_rev11_l2)
        self.lineEdit_rev11_l2.setMaxLength(4)
        self.lineEdit_rev11_l3.returnPressed.connect(self.send_to_rev11_l3)
        self.lineEdit_rev11_l3.setMaxLength(4)
        self.pushButton_save_log.clicked.connect(self.save_log)
        self.plainTextEdit_reg_fallos.textChanged.connect(self.enable_save_button)
        self.pushButton_save_log.setEnabled(False)

    def updateLCD(self, value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10,
                  value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, value21,
                  value22, value23):

        if sensor_flags[0] == 0:
            self.lcdNumber_rev3_r1.display(value9)
        elif sensor_flags[0] == 1:
            self.lcdNumber_rev3_r1.display(0)
        elif sensor_flags[0] == 2:
            pass
        elif sensor_flags[0] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_r1.display(value9 + 10)
        elif sensor_flags[0] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_r1.display(value9 + 0.5)
        elif sensor_flags[0] == 3 and canal == 'Par':
            self.lcdNumber_rev3_r1.display(value9 + 2)
        elif sensor_flags[0] == 4:
            self.lcdNumber_rev3_r1.display(round(value9 * 1.2))

        if sensor_flags[1] == 0:
            self.lcdNumber_rev3_r2.display(value10)
        elif sensor_flags[1] == 1:
            self.lcdNumber_rev3_r2.display(0)
        elif sensor_flags[1] == 2:
            pass
        elif sensor_flags[1] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_r2.display(value10 + 10)
        elif sensor_flags[1] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_r2.display(value10 + 0.5)
        elif sensor_flags[1] == 3 and canal == 'Par':
            self.lcdNumber_rev3_r2.display(value10 + 2)
        elif sensor_flags[1] == 4:
            self.lcdNumber_rev3_r2.display(round(value10 * 1.2))

        if sensor_flags[2] == 0:
            self.lcdNumber_rev3_r3.display(value11)
        elif sensor_flags[2] == 1:
            self.lcdNumber_rev3_r3.display(0)
        elif sensor_flags[2] == 2:
            pass
        elif sensor_flags[2] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_r3.display(value11 + 10)
        elif sensor_flags[2] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_r3.display(value11 + 0.5)
        elif sensor_flags[2] == 3 and canal == 'Par':
            self.lcdNumber_rev3_r3.display(value11 + 2)
        elif sensor_flags[2] == 4:
            self.lcdNumber_rev3_r3.display(round(value11 * 1.2))

        if sensor_flags[3] == 0:
            self.lcdNumber_rev3_l1.display(value6)
        elif sensor_flags[3] == 1:
            self.lcdNumber_rev3_l1.display(0)
        elif sensor_flags[3] == 2:
            pass
        elif sensor_flags[3] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_l1.display(value6 + 10)
        elif sensor_flags[3] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_l1.display(value6 + 0.5)
        elif sensor_flags[3] == 3 and canal == 'Par':
            self.lcdNumber_rev3_l1.display(value6 + 2)
        elif sensor_flags[3] == 4:
            self.lcdNumber_rev3_l1.display(round(value6 * 1.2))

        if sensor_flags[4] == 0:
            self.lcdNumber_rev3_l2.display(value7)
        elif sensor_flags[4] == 1:
            self.lcdNumber_rev3_l2.display(0)
        elif sensor_flags[4] == 2:
            pass
        elif sensor_flags[4] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_l2.display(value7 + 10)
        elif sensor_flags[4] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_l2.display(value7 + 0.5)
        elif sensor_flags[4] == 3 and canal == 'Par':
            self.lcdNumber_rev3_l2.display(value7 + 2)
        elif sensor_flags[4] == 4:
            self.lcdNumber_rev3_l2.display(round(value7 * 1.2))

        if sensor_flags[5] == 0:
            self.lcdNumber_rev3_l3.display(value8)
        elif sensor_flags[5] == 1:
            self.lcdNumber_rev3_l3.display(0)
        elif sensor_flags[5] == 2:
            pass
        elif sensor_flags[5] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev3_l3.display(value8 + 10)
        elif sensor_flags[5] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev3_l3.display(value8 + 0.5)
        elif sensor_flags[5] == 3 and canal == 'Par':
            self.lcdNumber_rev3_l3.display(value8 + 2)
        elif sensor_flags[5] == 4:
            self.lcdNumber_rev3_l3.display(round(value8 * 1.2))

        if sensor_flags[6] == 0:
            self.lcdNumber_rev5_r1.display(value15)
        elif sensor_flags[6] == 1:
            self.lcdNumber_rev5_r1.display(0)
        elif sensor_flags[6] == 2:
            pass
        elif sensor_flags[6] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_r1.display(value15 + 10)
        elif sensor_flags[6] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_r1.display(value15 + 0.5)
        elif sensor_flags[6] == 3 and canal == 'Par':
            self.lcdNumber_rev5_r1.display(value15 + 2)
        elif sensor_flags[6] == 4:
            self.lcdNumber_rev5_r1.display(round(value15 * 1.2))

        if sensor_flags[7] == 0:
            self.lcdNumber_rev5_r2.display(value16)
        elif sensor_flags[7] == 1:
            self.lcdNumber_rev5_r2.display(0)
        elif sensor_flags[7] == 2:
            pass
        elif sensor_flags[7] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_r2.display(value16 + 10)
        elif sensor_flags[7] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_r2.display(value16 + 0.5)
        elif sensor_flags[7] == 3 and canal == 'Par':
            self.lcdNumber_rev5_r2.display(value16 + 2)
        elif sensor_flags[7] == 4:
            self.lcdNumber_rev5_r2.display(round(value16 * 1.2))

        if sensor_flags[8] == 0:
            self.lcdNumber_rev5_r3.display(value17)
        elif sensor_flags[8] == 1:
            self.lcdNumber_rev5_r3.display(0)
        elif sensor_flags[8] == 2:
            pass
        elif sensor_flags[8] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_r3.display(value17 + 10)
        elif sensor_flags[8] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_r3.display(value17 + 0.5)
        elif sensor_flags[8] == 3 and canal == 'Par':
            self.lcdNumber_rev5_r3.display(value17 + 2)
        elif sensor_flags[8] == 4:
            self.lcdNumber_rev5_r3.display(round(value17 * 1.2))

        if sensor_flags[9] == 0:
            self.lcdNumber_rev5_l1.display(value12)
        elif sensor_flags[9] == 1:
            self.lcdNumber_rev5_l1.display(0)
        elif sensor_flags[9] == 2:
            pass
        elif sensor_flags[9] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_l1.display(value12 + 10)
        elif sensor_flags[9] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_l1.display(value12 + 0.5)
        elif sensor_flags[9] == 3 and canal == 'Par':
            self.lcdNumber_rev5_l1.display(value12 + 2)
        elif sensor_flags[9] == 4:
            self.lcdNumber_rev5_l1.display(round(value12 * 1.2))

        if sensor_flags[10] == 0:
            self.lcdNumber_rev5_l2.display(value13)
        elif sensor_flags[10] == 1:
            self.lcdNumber_rev5_l2.display(0)
        elif sensor_flags[10] == 2:
            pass
        elif sensor_flags[10] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_l2.display(value13 + 10)
        elif sensor_flags[10] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_l2.display(value13 + 0.5)
        elif sensor_flags[10] == 3 and canal == 'Par':
            self.lcdNumber_rev5_l2.display(value13 + 2)
        elif sensor_flags[10] == 4:
            self.lcdNumber_rev5_l2.display(round(value13 * 1.2))

        if sensor_flags[11] == 0:
            self.lcdNumber_rev5_l3.display(value14)
        elif sensor_flags[11] == 1:
            self.lcdNumber_rev5_l3.display(0)
        elif sensor_flags[11] == 2:
            pass
        elif sensor_flags[11] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev5_l3.display(value14 + 10)
        elif sensor_flags[11] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev5_l3.display(value14 + 0.5)
        elif sensor_flags[11] == 3 and canal == 'Par':
            self.lcdNumber_rev5_l3.display(value14 + 2)
        elif sensor_flags[11] == 4:
            self.lcdNumber_rev5_l3.display(round(value14 * 1.2))

        if sensor_flags[12] == 0:
            self.lcdNumber_rev8_r1.display(value21)
        elif sensor_flags[12] == 1:
            self.lcdNumber_rev8_r1.display(0)
        elif sensor_flags[12] == 2:
            pass
        elif sensor_flags[12] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_r1.display(value21 + 10)
        elif sensor_flags[12] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_r1.display(value21 + 0.5)
        elif sensor_flags[12] == 3 and canal == 'Par':
            self.lcdNumber_rev8_r1.display(value21 + 2)
        elif sensor_flags[12] == 4:
            self.lcdNumber_rev8_r1.display(round(value21 * 1.2))

        if sensor_flags[13] == 0:
            self.lcdNumber_rev8_r2.display(value22)
        elif sensor_flags[13] == 1:
            self.lcdNumber_rev8_r2.display(0)
        elif sensor_flags[13] == 2:
            pass
        elif sensor_flags[13] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_r2.display(value22 + 10)
        elif sensor_flags[13] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_r2.display(value22 + 0.5)
        elif sensor_flags[13] == 3 and canal == 'Par':
            self.lcdNumber_rev8_r2.display(value22 + 2)
        elif sensor_flags[13] == 4:
            self.lcdNumber_rev8_r2.display(round(value22 * 1.2))

        if sensor_flags[14] == 0:
            self.lcdNumber_rev8_r3.display(value23)
        elif sensor_flags[14] == 1:
            self.lcdNumber_rev8_r3.display(0)
        elif sensor_flags[14] == 2:
            pass
        elif sensor_flags[14] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_r3.display(value23 + 10)
        elif sensor_flags[14] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_r3.display(value23 + 0.5)
        elif sensor_flags[14] == 3 and canal == 'Par':
            self.lcdNumber_rev8_r3.display(value23 + 2)
        elif sensor_flags[14] == 4:
            self.lcdNumber_rev8_r3.display(round(value23 * 1.2))

        if sensor_flags[15] == 0:
            self.lcdNumber_rev8_l1.display(value18)
        elif sensor_flags[15] == 1:
            self.lcdNumber_rev8_l1.display(0)
        elif sensor_flags[15] == 2:
            pass
        elif sensor_flags[15] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_l1.display(value18 + 10)
        elif sensor_flags[15] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_l1.display(value18 + 0.5)
        elif sensor_flags[15] == 3 and canal == 'Par':
            self.lcdNumber_rev8_l1.display(value18 + 2)
        elif sensor_flags[15] == 4:
            self.lcdNumber_rev8_l1.display(round(value18 * 1.2))

        if sensor_flags[16] == 0:
            self.lcdNumber_rev8_l2.display(value19)
        elif sensor_flags[16] == 1:
            self.lcdNumber_rev8_l2.display(0)
        elif sensor_flags[16] == 2:
            pass
        elif sensor_flags[16] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_l2.display(value19 + 10)
        elif sensor_flags[16] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_l2.display(value19 + 0.5)
        elif sensor_flags[16] == 3 and canal == 'Par':
            self.lcdNumber_rev8_l2.display(value19 + 2)
        elif sensor_flags[16] == 4:
            self.lcdNumber_rev8_l2.display(round(value19 * 1.2))

        if sensor_flags[17] == 0:
            self.lcdNumber_rev8_l3.display(value20)
        elif sensor_flags[17] == 1:
            self.lcdNumber_rev8_l3.display(0)
        elif sensor_flags[17] == 2:
            pass
        elif sensor_flags[17] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev8_l3.display(value20 + 10)
        elif sensor_flags[17] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev8_l3.display(value20 + 0.5)
        elif sensor_flags[17] == 3 and canal == 'Par':
            self.lcdNumber_rev8_l3.display(value20 + 2)
        elif sensor_flags[17] == 4:
            self.lcdNumber_rev8_l3.display(round(value20 * 1.2))

        if sensor_flags[18] == 0:
            self.lcdNumber_rev11_r1.display(value3)
        elif sensor_flags[18] == 1:
            self.lcdNumber_rev11_r1.display(0)
        elif sensor_flags[18] == 2:
            pass
        elif sensor_flags[18] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_r1.display(value3 + 10)
        elif sensor_flags[18] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_r1.display(value3 + 0.5)
        elif sensor_flags[18] == 3 and canal == 'Par':
            self.lcdNumber_rev11_r1.display(value3 + 2)
        elif sensor_flags[18] == 4:
            self.lcdNumber_rev11_r1.display(round(value3 * 1.2))

        if sensor_flags[19] == 0:
            self.lcdNumber_rev11_r2.display(value4)
        elif sensor_flags[19] == 1:
            self.lcdNumber_rev11_r2.display(0)
        elif sensor_flags[19] == 2:
            pass
        elif sensor_flags[19] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_r2.display(value4 + 10)
        elif sensor_flags[19] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_r2.display(value4 + 0.5)
        elif sensor_flags[19] == 3 and canal == 'Par':
            self.lcdNumber_rev11_r2.display(value4 + 2)
        elif sensor_flags[19] == 4:
            self.lcdNumber_rev11_r2.display(round(value4 * 1.2))

        if sensor_flags[20] == 0:
            self.lcdNumber_rev11_r3.display(value5)
        elif sensor_flags[20] == 1:
            self.lcdNumber_rev11_r3.display(0)
        elif sensor_flags[20] == 2:
            pass
        elif sensor_flags[20] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_r3.display(value5 + 10)
        elif sensor_flags[20] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_r3.display(value5 + 0.5)
        elif sensor_flags[20] == 3 and canal == 'Par':
            self.lcdNumber_rev11_r3.display(value5 + 2)
        elif sensor_flags[20] == 4:
            self.lcdNumber_rev11_r3.display(round(value5 * 1.2))

        if sensor_flags[21] == 0:
            self.lcdNumber_rev11_l1.display(value0)
        elif sensor_flags[21] == 1:
            self.lcdNumber_rev11_l1.display(0)
        elif sensor_flags[21] == 2:
            pass
        elif sensor_flags[21] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_l1.display(value0 + 10)
        elif sensor_flags[21] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_l1.display(value0 + 0.5)
        elif sensor_flags[21] == 3 and canal == 'Par':
            self.lcdNumber_rev11_l1.display(value0 + 2)
        elif sensor_flags[21] == 4:
            self.lcdNumber_rev11_l1.display(value0 * 1.2)

        if sensor_flags[22] == 0:
            self.lcdNumber_rev11_l2.display(value1)
        elif sensor_flags[22] == 1:
            self.lcdNumber_rev11_l2.display(0)
        elif sensor_flags[22] == 2:
            pass
        elif sensor_flags[22] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_l2.display(value1 + 10)
        elif sensor_flags[22] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_l2.display(value1 + 0.5)
        elif sensor_flags[22] == 3 and canal == 'Par':
            self.lcdNumber_rev11_l2.display(value1 + 2)
        elif sensor_flags[22] == 4:
            self.lcdNumber_rev11_l2.display(round(value1 * 1.2))

        if sensor_flags[23] == 0:
            self.lcdNumber_rev11_l3.display(value2)
        elif sensor_flags[23] == 1:
            self.lcdNumber_rev11_l3.display(0)
        elif sensor_flags[23] == 2:
            pass
        elif sensor_flags[23] == 3 and canal == 'Ángulo':
            self.lcdNumber_rev11_l3.display(value2 + 10)
        elif sensor_flags[23] == 3 and canal == 'Velocidad angular':
            self.lcdNumber_rev11_l3.display(value2 + 0.5)
        elif sensor_flags[23] == 3 and canal == 'Par':
            self.lcdNumber_rev11_l3.display(value2 + 2)
        elif sensor_flags[23] == 4:
            self.lcdNumber_rev11_l3.display(round(value2 * 1.2))


    @pyqtSlot()
    def disableButton_enpie(self):
        self.pushButton_en_pie.setEnabled(False)
        self.pushButton_anda.setEnabled(False)

    @pyqtSlot()
    def reenableButton_enpie(self):
        self.pushButton_en_pie.setEnabled(True)
        self.pushButton_anda.setEnabled(True)

    @pyqtSlot()
    def paro_andatalker(self):
        self.comboBox_met.setEnabled(True)
        self.pushButton_en_pie.setEnabled(True)
        if self.comboBox_met.currentText() == 'Algoritmo 1':
            self.anda.flag = True
        elif self.comboBox_met.currentText() == 'Algoritmo 2':
            self.anda2.flag = True

    @pyqtSlot()
    def disconnect_from_andatalker(self):
        #print('Desconectado de andatalker')
        self.comboBox_met.setEnabled(False)
        self.pushButton_en_pie.setEnabled(False)
        if self.comboBox_met.currentText() == 'Algoritmo 1':
            try:
                self.pushButton_anda.clicked.disconnect(self.anda.talker)
            except Exception:
                pass
        elif self.comboBox_met.currentText() == 'Algoritmo 2':
            try:
                self.pushButton_anda.clicked.disconnect(self.anda2.talker)
            except Exception:
                pass

        self.pushButton_anda.clicked.connect(self.paro_andatalker)
        #print('Conectado a paro_andatalker')

    @pyqtSlot()
    def reconnect_to_andatalker(self):
        if self.comboBox_met.currentText() == 'Algoritmo 1':
            self.pushButton_anda.clicked.connect(self.anda.talker)
        elif self.comboBox_met.currentText() == 'Algoritmo 2':
            self.pushButton_anda.clicked.connect(self.anda2.talker)

        self.pushButton_anda.clicked.disconnect(self.paro_andatalker)


    def setupThreads(self):
        # Hilo para ponerlo en pie
        self.thread = QThread()
        self.enpie = depie_talker()
        self.enpie.moveToThread(self.thread)
        self.thread.started.connect(self.enpie.run)
        self.pushButton_en_pie.clicked.connect(self.enpie.talker)
        self.enpie.wait_for_input.connect(self.disableButton_enpie)
        self.enpie.done.connect(self.reenableButton_enpie)

        # Hilo para órdenes individuales
        self.thread2 = QThread()
        self.set_pos = set_pos()
        self.set_pos.moveToThread(self.thread2)
        self.thread2.started.connect(self.set_pos.run)
        # Conectamos
        self.msg.connect(self.set_pos.talker2)

        #Hilo para andar método 1
        self.thread3 = QThread()
        self.anda = anda_talker()
        self.anda.moveToThread(self.thread3)
        self.thread3.started.connect(self.anda.run)
        self.pushButton_anda.clicked.connect(self.anda.talker)
        self.pushButton_anda.setEnabled(False)
        self.anda.wait_for_input.connect(self.disconnect_from_andatalker)
        self.anda.done.connect(self.reconnect_to_andatalker)

        #Hilo para andar método 2
        self.thread4 = QThread()
        self.anda2 = anda_talker2()
        self.anda2.moveToThread(self.thread4)
        self.thread4.started.connect(self.anda2.run)
        self.anda2.wait_for_input.connect(self.disconnect_from_andatalker)
        self.anda2.done.connect(self.reconnect_to_andatalker)

        # Start threads
        self.thread.start()
        self.thread2.start()
        self.thread3.start()
        self.thread4.start()

    def set_alg(self, text):
        if text == 'Algoritmo 1':
            try:
                self.pushButton_anda.clicked.disconnect(self.anda2.talker)
            except Exception:
                pass
            self.pushButton_anda.clicked.connect(self.anda.talker)

        if text == 'Algoritmo 2':
            try:
                self.pushButton_anda.clicked.disconnect(self.anda.talker)
            except Exception:
                pass
            self.pushButton_anda.clicked.connect(self.anda2.talker)

    def send_to_rev3_r1(self):
        art = "Rev3_r_1"
        if self.lineEdit_rev3_r1.text() == 'a':
            client_Rev3_r_1.update_configuration(params_a)
            client_Rev3_r_1_biased.update_configuration(params_a)
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'b':
            client_Rev3_r_1.update_configuration(params_b2)
            client_Rev3_r_1_biased.update_configuration(params_b2)
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_r_1_biased_position_controller'], ['Rev3_r_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'f':
            sensor_flags[0] = 1
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'g':
            sensor_flags[0] = 2
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'h':
            sensor_flags[0] = 3
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_r1.text() == 'i':
            sensor_flags[0] = 4
            self.lineEdit_rev3_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_r1.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r1", "Rev3", pos)
                self.lineEdit_rev3_r1.clear()

    def send_to_rev3_r2(self):
        art = "Rev3_r_2"
        if self.lineEdit_rev3_r2.text() == 'a':
            client_Rev3_r_2.update_configuration(params_a)
            client_Rev3_r_2_biased.update_configuration(params_a)
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'b':
            client_Rev3_r_2.update_configuration(params_b2)
            client_Rev3_r_2_biased.update_configuration(params_b2)
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_r_2_biased_position_controller'], ['Rev3_r_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'f':
            sensor_flags[1] = 1
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'g':
            sensor_flags[1] = 2
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'h':
            sensor_flags[1] = 3
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_r2.text() == 'i':
            sensor_flags[1] = 4
            self.lineEdit_rev3_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_r2.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r2", "Rev3", pos)
                self.lineEdit_rev3_r2.clear()

    def send_to_rev3_r3(self):
        art = "Rev3_r_3"
        if self.lineEdit_rev3_r3.text() == 'a':
            client_Rev3_r_3.update_configuration(params_a)
            client_Rev3_r_3_biased.update_configuration(params_a)
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'b':
            client_Rev3_r_3.update_configuration(params_b2)
            client_Rev3_r_3_biased.update_configuration(params_b2)
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_r_3_biased_position_controller'], ['Rev3_r_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'f':
            sensor_flags[2] = 1
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'g':
            sensor_flags[2] = 2
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'h':
            sensor_flags[2] = 3
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_r3.text() == 'i':
            sensor_flags[2] = 4
            self.lineEdit_rev3_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_r3.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r3", "Rev3", pos)
                self.lineEdit_rev3_r3.clear()

    def send_to_rev3_l1(self):
        art = "Rev3_l_1"
        if self.lineEdit_rev3_l1.text() == 'a':
            client_Rev3_l_1.update_configuration(params_a)
            client_Rev3_l_1_biased.update_configuration(params_a)
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'b':
            client_Rev3_l_1.update_configuration(params_b2)
            client_Rev3_l_1_biased.update_configuration(params_b2)
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_l_1_biased_position_controller'], ['Rev3_l_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'f':
            sensor_flags[3] = 1
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'g':
            sensor_flags[3] = 2
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'h':
            sensor_flags[3] = 3
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_l1.text() == 'i':
            sensor_flags[3] = 4
            self.lineEdit_rev3_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_l1.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l1", "Rev3", pos)
                self.lineEdit_rev3_l1.clear()

    def send_to_rev3_l2(self):
        art = "Rev3_l_2"
        if self.lineEdit_rev3_l2.text() == 'a':
            client_Rev3_l_2.update_configuration(params_a)
            client_Rev3_l_2_biased.update_configuration(params_a)
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'b':
            client_Rev3_l_2.update_configuration(params_b2)
            client_Rev3_l_2_biased.update_configuration(params_b2)
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_l_2_biased_position_controller'], ['Rev3_l_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'f':
            sensor_flags[4] = 1
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'g':
            sensor_flags[4] = 2
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'h':
            sensor_flags[4] = 3
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_l2.text() == 'i':
            sensor_flags[4] = 4
            self.lineEdit_rev3_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_l2.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l2", "Rev3", pos)
                self.lineEdit_rev3_l2.clear()

    def send_to_rev3_l3(self):
        art = "Rev3_l_3"
        if self.lineEdit_rev3_l3.text() == 'a':
            client_Rev3_l_3.update_configuration(params_a)
            client_Rev3_l_3_biased.update_configuration(params_a)
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'b':
            client_Rev3_l_3.update_configuration(params_b2)
            client_Rev3_l_3_biased.update_configuration(params_b2)
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev3_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev3_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev3_l_3_biased_position_controller'], ['Rev3_l_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'f':
            sensor_flags[5] = 1
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'g':
            sensor_flags[5] = 2
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'h':
            sensor_flags[5] = 3
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev3_l3.text() == 'i':
            sensor_flags[5] = 4
            self.lineEdit_rev3_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev3_l3.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l3", "Rev3", pos)
                self.lineEdit_rev3_l3.clear()

    def send_to_rev5_r1(self):
        art = "Rev5_r_1"
        if self.lineEdit_rev5_r1.text() == 'a':
            client_Rev5_r_1.update_configuration(params_a)
            client_Rev5_r_1_biased.update_configuration(params_a)
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'b':
            client_Rev5_r_1.update_configuration(params_b1)
            client_Rev5_r_1_biased.update_configuration(params_b1)
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev5_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_r_1_biased_position_controller'], ['Rev5_r_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'f':
            sensor_flags[6] = 1
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'g':
            sensor_flags[6] = 2
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'h':
            sensor_flags[6] = 3
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_r1.text() == 'i':
            sensor_flags[6] = 4
            self.lineEdit_rev5_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_r1.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r1", "Rev5", pos)
                self.lineEdit_rev5_r1.clear()

    def send_to_rev5_r2(self):
        art = "Rev5_r_2"
        if self.lineEdit_rev5_r2.text() == 'a':
            client_Rev5_r_2.update_configuration(params_a)
            client_Rev5_r_2_biased.update_configuration(params_a)
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'b':
            client_Rev5_r_2.update_configuration(params_b1)
            client_Rev5_r_2_biased.update_configuration(params_b1)
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_2")
                service("Rev5_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_r_2_biased_position_controller'], ['Rev5_r_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'f':
            sensor_flags[7] = 1
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'g':
            sensor_flags[7] = 2
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'h':
            sensor_flags[7] = 3
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_r2.text() == 'i':
            sensor_flags[7] = 4
            self.lineEdit_rev5_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_r2.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r2", "Rev5", pos)
                self.lineEdit_rev5_r2.clear()

    def send_to_rev5_r3(self):
        art = "Rev5_r_3"
        if self.lineEdit_rev5_r3.text() == 'a':
            client_Rev5_r_3.update_configuration(params_a)
            client_Rev5_r_3_biased.update_configuration(params_a)
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'b':
            client_Rev5_r_3.update_configuration(params_b1)
            client_Rev5_r_3_biased.update_configuration(params_b1)
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_3")
                service("Rev5_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_r_3_biased_position_controller'], ['Rev5_r_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'f':
            sensor_flags[8] = 1
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'g':
            sensor_flags[8] = 2
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'h':
            sensor_flags[8] = 3
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_r3.text() == 'i':
            sensor_flags[8] = 4
            self.lineEdit_rev5_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_r3.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata r3", "Rev5", pos)
                self.lineEdit_rev5_r3.clear()

    def send_to_rev5_l1(self):
        art = "Rev5_l_1"
        if self.lineEdit_rev5_l1.text() == 'a':
            client_Rev5_l_1.update_configuration(params_a)
            client_Rev5_l_1_biased.update_configuration(params_a)
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'b':
            client_Rev5_l_1.update_configuration(params_b1)
            client_Rev5_l_1_biased.update_configuration(params_b1)
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_1")
                service("Rev5_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_l_1_biased_position_controller'], ['Rev5_l_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'f':
            sensor_flags[9] = 1
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'g':
            sensor_flags[9] = 2
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'h':
            sensor_flags[9] = 3
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_l1.text() == 'i':
            sensor_flags[9] = 4
            self.lineEdit_rev5_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_l1.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l1", "Rev5", pos)
                self.lineEdit_rev5_l1.clear()

    def send_to_rev5_l2(self):
        art = "Rev5_l_2"
        if self.lineEdit_rev5_l2.text() == 'a':
            client_Rev5_l_2.update_configuration(params_a)
            client_Rev5_l_2_biased.update_configuration(params_a)
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'b':
            client_Rev5_l_2.update_configuration(params_b1)
            client_Rev5_l_2_biased.update_configuration(params_b1)
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_2")
                service("Rev5_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_l_2_biased_position_controller'], ['Rev5_l_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'f':
            sensor_flags[10] = 1
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'g':
            sensor_flags[10] = 2
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'h':
            sensor_flags[10] = 3
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_l2.text() == 'i':
            sensor_flags[10] = 4
            self.lineEdit_rev5_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_l2.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l2", "Rev5", pos)
                self.lineEdit_rev5_l2.clear()

    def send_to_rev5_l3(self):
        art = "Rev5_l_3"
        if self.lineEdit_rev5_l3.text() == 'a':
            client_Rev5_l_3.update_configuration(params_a)
            client_Rev5_l_3_biased.update_configuration(params_a)
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'b':
            client_Rev5_l_3.update_configuration(params_b1)
            client_Rev5_l_3_biased.update_configuration(params_b1)
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_3")
                service("Rev5_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev5_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev5_l_3_biased_position_controller'], ['Rev5_l_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'f':
            sensor_flags[11] = 1
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'g':
            sensor_flags[11] = 2
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'h':
            sensor_flags[11] = 3
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev5_l3.text() == 'i':
            sensor_flags[11] = 4
            self.lineEdit_rev5_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev5_l3.text())
            if (pos >= -110 and pos <= 110):
                self.msg.emit("Pata l3", "Rev5", pos)
                self.lineEdit_rev5_l3.clear()

    def send_to_rev8_r1(self):
        art = "Rev8_r_1"
        if self.lineEdit_rev8_r1.text() == 'a':
            client_Rev8_r_1.update_configuration(params_a)
            client_Rev8_r_1_biased.update_configuration(params_a)
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'b':
            client_Rev8_r_1.update_configuration(params_b1)
            client_Rev8_r_1_biased.update_configuration(params_b1)
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev8_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_r_1_biased_position_controller'], ['Rev8_r_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'f':
            sensor_flags[12] = 1
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'g':
            sensor_flags[12] = 2
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'h':
            sensor_flags[12] = 3
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_r1.text() == 'i':
            sensor_flags[12] = 4
            self.lineEdit_rev8_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_r1.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata r1", "Rev8", pos)
                self.lineEdit_rev8_r1.clear()

    def send_to_rev8_r2(self):
        art = "Rev8_r_2"
        if self.lineEdit_rev8_r2.text() == 'a':
            client_Rev8_r_2.update_configuration(params_a)
            client_Rev8_r_2_biased.update_configuration(params_a)
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'b':
            client_Rev8_r_2.update_configuration(params_b1)
            client_Rev8_r_2_biased.update_configuration(params_b1)
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_2")
                service("Rev8_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_r_2_biased_position_controller'], ['Rev8_r_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'f':
            sensor_flags[13] = 1
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'g':
            sensor_flags[13] = 2
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'h':
            sensor_flags[13] = 3
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_r2.text() == 'i':
            sensor_flags[13] = 4
            self.lineEdit_rev8_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_r2.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata r2", "Rev8", pos)
                self.lineEdit_rev8_r2.clear()

    def send_to_rev8_r3(self):
        art = "Rev8_r_3"
        if self.lineEdit_rev8_r3.text() == 'a':
            client_Rev8_r_3.update_configuration(params_a)
            client_Rev8_r_3_biased.update_configuration(params_a)
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'b':
            client_Rev8_r_3.update_configuration(params_b1)
            client_Rev8_r_3_biased.update_configuration(params_b1)
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_3")
                service("Rev8_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r3clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_r_3_biased_position_controller'], ['Rev8_r_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'f':
            sensor_flags[14] = 1
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'g':
            sensor_flags[14] = 2
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'h':
            sensor_flags[14] = 3
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_r3.text() == 'i':
            sensor_flags[14] = 4
            self.lineEdit_rev8_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_r3.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata r3", "Rev8", pos)
                self.lineEdit_rev8_r3.clear()

    def send_to_rev8_l1(self):
        art = "Rev8_l_1"
        if self.lineEdit_rev8_l1.text() == 'a':
            client_Rev8_l_1.update_configuration(params_a)
            client_Rev8_l_1_biased.update_configuration(params_a)
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'b':
            client_Rev8_l_1.update_configuration(params_b1)
            client_Rev8_l_1_biased.update_configuration(params_b1)
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_1")
                service("Rev8_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_l_1_biased_position_controller'], ['Rev8_l_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'f':
            sensor_flags[15] = 1
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'g':
            sensor_flags[15] = 2
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'h':
            sensor_flags[15] = 3
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_l1.text() == 'i':
            sensor_flags[15] = 4
            self.lineEdit_rev8_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_l1.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata l1", "Rev8", pos)
                self.lineEdit_rev8_l1.clear()

    def send_to_rev8_l2(self):
        art = "Rev8_l_2"
        if self.lineEdit_rev8_l2.text() == 'a':
            client_Rev8_l_2.update_configuration(params_a)
            client_Rev8_l_2_biased.update_configuration(params_a)
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'b':
            client_Rev8_l_2.update_configuration(params_b1)
            client_Rev8_l_2_biased.update_configuration(params_b1)
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_2")
                service("Rev8_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_l_2_biased_position_controller'], ['Rev8_l_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'f':
            sensor_flags[16] = 1
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'g':
            sensor_flags[16] = 2
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'h':
            sensor_flags[16] = 3
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_l2.text() == 'i':
            sensor_flags[16] = 4
            self.lineEdit_rev8_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_l2.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata l2", "Rev8", pos)
                self.lineEdit_rev8_l2.clear()

    def send_to_rev8_l3(self):
        art = "Rev8_l_3"
        if self.lineEdit_rev8_l3.text() == 'a':
            client_Rev8_l_3.update_configuration(params_a)
            client_Rev8_l_3_biased.update_configuration(params_a)
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'b':
            client_Rev8_l_3.update_configuration(params_b1)
            client_Rev8_l_3_biased.update_configuration(params_b1)
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_3")
                service("Rev8_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev8_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev8_l_3_biased_position_controller'], ['Rev8_l_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'f':
            sensor_flags[17] = 1
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'g':
            sensor_flags[17] = 2
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'h':
            sensor_flags[17] = 3
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev8_l3.text() == 'i':
            sensor_flags[17] = 4
            self.lineEdit_rev8_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev8_l3.text())
            if (pos >= -45 and pos <= 180):
                self.msg.emit("Pata l3", "Rev8", pos)
                self.lineEdit_rev8_l3.clear()

    def send_to_rev11_r1(self):
        art = "Rev11_r_1"
        if self.lineEdit_rev11_r1.text() == 'a':
            client_Rev11_r_1_.update_configuration(params_a)
            client_Rev11_r_1_biased.update_configuration(params_a)
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'b':
            client_Rev11_r_1.update_configuration(params_b2)
            client_Rev11_r_1_biased.update_configuration(params_b2)
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                service("Rev11_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_r_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_r_1_biased_position_controller'], ['Rev11_r_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'f':
            sensor_flags[18] = 1
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'g':
            sensor_flags[18] = 2
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'h':
            sensor_flags[18] = 3
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_r1.text() == 'i':
            sensor_flags[18] = 4
            self.lineEdit_rev11_r1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev11_r1.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata r1", "Rev11", pos)
                self.lineEdit_rev11_r1.clear()

    def send_to_rev11_r2(self):
        art = "Rev11_r_2"
        if self.lineEdit_rev11_r2.text() == 'a':
            client_Rev11_r_2.update_configuration(params_a)
            client_Rev11_r_2_biased.update_configuration(params_a)
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'b':
            client_Rev11_r_2.update_configuration(params_b2)
            client_Rev11_r_2_biased.update_configuration(params_b2)
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_2")
                service("Rev11_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_r_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_r_2_biased_position_controller'], ['Rev11_r_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'f':
            sensor_flags[19] = 1
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'g':
            sensor_flags[19] = 2
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'h':
            sensor_flags[19] = 3
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_r2.text() == 'i':
            sensor_flags[19] = 4
            self.lineEdit_rev11_r2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev11_r2.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata r2", "Rev11", pos)
                self.lineEdit_rev11_r2.clear()

    def send_to_rev11_r3(self):
        art = "Rev11_r_3"
        if self.lineEdit_rev11_r3.text() == 'a':
            client_Rev11_r_3.update_configuration(params_a)
            client_Rev11_r_3_biased.update_configuration(params_a)
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'b':
            client_Rev11_r_3.update_configuration(params_b2)
            client_Rev11_r_3_biased.update_configuration(params_b2)
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_r_3")
                service("Rev11_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_r_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_r_3_biased_position_controller'], ['Rev11_r_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'f':
            sensor_flags[20] = 1
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'g':
            sensor_flags[20] = 2
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'h':
            sensor_flags[20] = 3
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_r3.text() == 'i':
            sensor_flags[20] = 4
            self.lineEdit_rev11_r3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev11_r3.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata r3", "Rev11", pos)
                self.lineEdit_rev11_r3.clear()

    def send_to_rev11_l1(self):
        art = "Rev11_l_1"
        if self.lineEdit_rev11_l1.text() == 'a':
            client_Rev11_l_1.update_configuration(params_a)
            client_Rev11_l_1_biased.update_configuration(params_a)
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'b':
            client_Rev11_l_1.update_configuration(params_b2)
            client_Rev11_l_1_biased.update_configuration(params_b2)
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_1")
                service("Rev11_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_l_1")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_l_1_biased_position_controller'], ['Rev11_l_1_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'f':
            sensor_flags[21] = 1
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'g':
            sensor_flags[21] = 2
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'h':
            sensor_flags[21] = 3
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_l1.text() == 'i':
            sensor_flags[21] = 4
            self.lineEdit_rev11_l1.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev11_l1.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata l1", "Rev11", pos)
                self.lineEdit_rev11_l1.clear()

    def send_to_rev11_l2(self):
        art = "Rev11_l_2"
        if self.lineEdit_rev11_l2.text() == 'a':
            client_Rev11_l_2.update_configuration(params_a)
            client_Rev11_l_2_biased.update_configuration(params_a)
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'b':
            client_Rev11_l_2.update_configuration(params_b2)
            client_Rev11_l_2_biased.update_configuration(params_b2)
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_2")
                service("Rev11_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_l_2")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_l_2_biased_position_controller'], ['Rev11_l_2_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'f':
            sensor_flags[22] = 1
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'g':
            sensor_flags[22] = 2
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'h':
            sensor_flags[22] = 3
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_l2.text() == 'i':
            sensor_flags[22] = 4
            self.lineEdit_rev11_l2.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:
            pos = int(self.lineEdit_rev11_l2.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata l2", "Rev11", pos)
                self.lineEdit_rev11_l2.clear()

    def send_to_rev11_l3(self):
        art = "Rev11_l_3"
        if self.lineEdit_rev11_l3.text() == 'a':
            client_Rev11_l_3.update_configuration(params_a)
            client_Rev11_l_3_biased.update_configuration(params_a)
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'a' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'b':
            client_Rev11_l_3.update_configuration(params_b2)
            client_Rev11_l_3_biased.update_configuration(params_b2)
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'b' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'c':
            rospy.wait_for_service('drop_joint')
            try:
                service = rospy.ServiceProxy('drop_joint', robominer_srv)
                #service("Rev3_l_3")
                service("Rev11_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'c' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'd':
            rospy.wait_for_service('lock_joint')
            try:
                service = rospy.ServiceProxy('lock_joint', robominer_srv)
                service("Rev11_l_3")
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'd' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'e':
            rospy.wait_for_service('/robominer/controller_manager/switch_controller')
            try:
                service = rospy.ServiceProxy('/robominer/controller_manager/switch_controller', SwitchController)
                service(['Rev11_l_3_biased_position_controller'], ['Rev11_l_3_position_controller'], 2, 1, 5)
            except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'e' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'f':
            sensor_flags[23] = 1
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'f' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'g':
            sensor_flags[23] = 2
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'g' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'h':
            sensor_flags[23] = 3
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'h' en " + art)
        elif self.lineEdit_rev11_l3.text() == 'i':
            sensor_flags[23] = 4
            self.lineEdit_rev11_l3.clear()
            self.plainTextEdit_reg_fallos.appendPlainText("Fallo 'i' en " + art)
        else:

            pos = int(self.lineEdit_rev11_l3.text())
            if (pos >= -90 and pos <= 90):
                self.msg.emit("Pata l3", "Rev11", pos)
                self.lineEdit_rev11_l3.clear()

    def show_lim(self, text):
        # Limites: Rev3: -110 110 Rev5: -110 110 Rev8: -45 180 Rev11: -90 90
        if text == 'Elija articulación':
            self.label_limits.setText('Rango:')
        if text == 'Rev3':
            self.label_limits.setText('Rango: [-110,110]º')
        if text == 'Rev5':
            self.label_limits.setText('Rango: [-110,110]º')
        if text == 'Rev8':
            self.label_limits.setText('Rango: [-45,180]º')
        if text == 'Rev11':
            self.label_limits.setText('Rango: [-90,90]º')


    def show_fallo(self, text):
        if text == 'Seleccione fallo':
            self.label_cod_fallos.setText('Código:')
        if text == 'Motor inhab.':
            self.label_cod_fallos.setText('Código: a')
        if text == 'Motor débil':
            self.label_cod_fallos.setText('Código: b')
        if text == 'Desanclar art.':
            self.label_cod_fallos.setText('Código: c')
        if text == 'Motor bloqueado':
            self.label_cod_fallos.setText('Código: d')
        if text == 'Motor desviado':
            self.label_cod_fallos.setText('Código: e')
        if text == 'Sensor valor nulo':
            self.label_cod_fallos.setText('Código: f')
        if text == 'Sensor valor fijo':
            self.label_cod_fallos.setText('Código: g')
        if text == 'Sensor error fijo':
            self.label_cod_fallos.setText('Código: h')
        if text == 'Sensor error prop.':
            self.label_cod_fallos.setText('Código: i')

    def set_canal(self, text):
        for i, val in enumerate(sensor_flags):
            if sensor_flags[i] != 0:
                fallo_sens = True
                sensor_flags[i] = 0
        if fallo_sens:
            self.plainTextEdit_reg_fallos.appendPlainText("Sensores reiniciados")
            fallo_sens = False

        try:
            self.pos.msg.disconnect(self.updateLCD)
        except Exception:
            pass
        try:
            self.vel.msg.disconnect(self.updateLCD)
        except Exception:
            pass
        try:
            self.par.msg.disconnect(self.updateLCD)
        except Exception:
            pass
        if text == 'Ángulo':
            self.label_tit.setText('Ángulo de cada articulación (º)')
            self.pos.msg.connect(self.updateLCD)
            canal = 'Ángulo'
        if text == 'Velocidad angular':
            self.label_tit.setText('Velocidad angular de cada articulación (rad/s)')
            self.vel.msg.connect(self.updateLCD)
            canal = 'Velocidad angular'
        if text == 'Par':
            self.label_tit.setText('Par de cada articulación (Nm)')
            self.par.msg.connect(self.updateLCD)
            canal = 'Par'
        self.comboBox_canal.setCurrentText("Seleccione canal")

    def save_log(self):
        logfilename = 'log ' + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        path = "/home/antonio/Documents/TFM/Registros de fallos/" + logfilename
        #f = open("/home/antonio/Documents/TFM/Registros de fallos/log", "a+")
        f = open(path, "a+")
        f.write(self.plainTextEdit_reg_fallos.toPlainText())
        f.close()

    def enable_save_button(self):
        self.pushButton_save_log.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())