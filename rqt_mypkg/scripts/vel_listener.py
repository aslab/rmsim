#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np

class vel_listener(QThread):

	msg = pyqtSignal(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)

	def callback(self,data):
		rospy.sleep(.1)
		'''
		for i, val in enumerate(data.velocity):
			if val > 0.75:
				data.velocity[i] = 0.75
			elif val < -0.75:
				data.velocity[i] = -0.75
		'''
		#np.clip(data.velocity, -0.75, 0.75)

		data.velocity = [-0.75 if x < -0.75 else 0.75 if x > 0.75 else x for x in data.velocity]

		self.msg.emit(data.velocity[0], data.velocity[1], data.velocity[2], data.velocity[3], data.velocity[4], data.velocity[5], data.velocity[6],
					  data.velocity[7],
					  data.velocity[8], data.velocity[9], data.velocity[10], data.velocity[11], data.velocity[12], data.velocity[13],
					  data.velocity[14], data.velocity[15],
					  data.velocity[16], data.velocity[17], data.velocity[18], data.velocity[19], data.velocity[20], data.velocity[21],
					  data.velocity[22], data.velocity[23])

	def listener(self):
		# rospy.init_node('robominer_joint_position_subscriber', anonymous=True)
		rospy.Subscriber("robominer/joint_states", JointState, self.callback, queue_size=1, buff_size=65536)
		rospy.spin()

	def run(self):
		self.listener()