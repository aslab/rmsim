#!/usr/bin/env python

import sys
from lcd_pos_ui import *
#import rospy
#import time
#from pos_listener import *
from rand_n_gen import *

#rospy.init_node('robominer_joint_position_subscriber', anonymous=True)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.num = rand_n_gen()
        self.num.msg.connect(self.updateLCD)
        self.num.start()
            #print(pos[9])

    def updateLCD(self,value):
        self.lcdNumber.display(value)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())