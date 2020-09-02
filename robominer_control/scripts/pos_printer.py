#!/usr/bin/env python

from pos_listener import *
from threading import Thread
import rospy

rospy.init_node('robominer_joint_position_subscriber', anonymous=True)

th1 = Thread(target=listener)
th1.start()

global pos
for x in range(10):
    rospy.sleep(1)
    print(pos_listener.pos[1])