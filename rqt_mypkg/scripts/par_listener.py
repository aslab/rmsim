#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from PyQt5.QtCore import QThread, pyqtSignal
from math import pi

class par_listener(QThread):

	msg = pyqtSignal(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)

	def callback(self,data):
		rospy.sleep(.1)
		self.msg.emit(data.effort[0], data.effort[1], data.effort[2], data.effort[3], data.effort[4], data.effort[5], data.effort[6],
					  data.effort[7],
					  data.effort[8], data.effort[9], data.effort[10], data.effort[11], data.effort[12], data.effort[13],
					  data.effort[14], data.effort[15],
					  data.effort[16], data.effort[17], data.effort[18], data.effort[19], data.effort[20], data.effort[21],
					  data.effort[22], data.effort[23])

	def listener(self):
		# rospy.init_node('robominer_joint_position_subscriber', anonymous=True)
		rospy.Subscriber("robominer/joint_states", JointState, self.callback, queue_size=1, buff_size=65536)
		rospy.spin()

	def run(self):
		self.listener()