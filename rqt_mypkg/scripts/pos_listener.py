#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from PyQt5.QtCore import QThread, pyqtSignal
from math import pi

class pos_listener(QThread):

	msg = pyqtSignal(float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)

	def callback(self,data):
		rospy.sleep(.1)
		ang_grad = [i * 180/pi for i in data.position]
		length = len(ang_grad)
		for x in range(length):
			ang_grad[x] = round(ang_grad[x])

		self.msg.emit(ang_grad[0],ang_grad[1],ang_grad[2],ang_grad[3],ang_grad[4],ang_grad[5],ang_grad[6],ang_grad[7],
					  ang_grad[8],ang_grad[9],ang_grad[10],ang_grad[11],ang_grad[12],ang_grad[13],ang_grad[14],ang_grad[15],
					  ang_grad[16],ang_grad[17],ang_grad[18],ang_grad[19],ang_grad[20],ang_grad[21],ang_grad[22],ang_grad[23])

	def listener(self):
		# rospy.init_node('robominer_joint_position_subscriber', anonymous=True)
		rospy.Subscriber("robominer/joint_states", JointState, self.callback, queue_size=1, buff_size=65536)
		rospy.spin()

	def run(self):
		self.listener()

#if __name__ == '__main__':
#    listener()


