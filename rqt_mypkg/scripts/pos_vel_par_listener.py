#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
from PyQt5.QtCore import *
from math import pi

class pos_vel_par_listener(QObject):

	msg = pyqtSignal(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)

	def callback_pos(self,data):
		rospy.sleep(.1)
		ang_grad = [i * 180/pi for i in data.position]
		length = len(ang_grad)
		for x in range(length):
			ang_grad[x] = round(ang_grad[x])

		self.msg.emit(ang_grad[0],ang_grad[1],ang_grad[2],ang_grad[3],ang_grad[4],ang_grad[5],ang_grad[6],ang_grad[7],
					  ang_grad[8],ang_grad[9],ang_grad[10],ang_grad[11],ang_grad[12],ang_grad[13],ang_grad[14],ang_grad[15],
					  ang_grad[16],ang_grad[17],ang_grad[18],ang_grad[19],ang_grad[20],ang_grad[21],ang_grad[22],ang_grad[23])

	def callback_vel(self, data):
		rospy.sleep(.1)
		self.msg.emit(data.velocity[0], data.velocity[1], data.velocity[2], data.velocity[3], data.velocity[4], data.velocity[5], data.velocity[6],
					  data.velocity[7],
					  data.velocity[8], data.velocity[9], data.velocity[10], data.velocity[11], data.velocity[12], data.velocity[13],
					  data.velocity[14], data.velocity[15],
					  data.velocity[16], data.velocity[17], data.velocity[18], data.velocity[19], data.velocity[20], data.velocity[21],
					  data.velocity[22], data.velocity[23])

	def callback_par(self, data):
		rospy.sleep(.1)
		self.msg.emit(data.effort[0], data.effort[1], data.effort[2], data.effort[3], data.effort[4], data.effort[5], data.effort[6],
					  data.effort[7],
					  data.effort[8], data.effort[9], data.effort[10], data.effort[11], data.effort[12], data.effort[13],
					  data.effort[14], data.effort[15],
					  data.effort[16], data.effort[17], data.effort[18], data.effort[19], data.effort[20], data.effort[21],
					  data.effort[22], data.effort[23])

	def listener(self,canal):
		if canal == "Ángulo":
			rospy.Subscriber("robominer/joint_states", JointState, self.callback_pos, queue_size=1, buff_size=65536)
			rospy.spin()
		if canal == "Velocidad angular":
			rospy.Subscriber("robominer/joint_states", JointState, self.callback_vel, queue_size=1, buff_size=65536)
			rospy.spin()
		if canal == "Par":
			rospy.Subscriber("robominer/joint_states", JointState, self.callback_par, queue_size=1, buff_size=65536)
			rospy.spin()

	def run(self):
		pass

#if __name__ == '__main__':
#    listener()


