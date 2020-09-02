#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
#from control_msgs.msg import FollowJointTrajectoryActionResult
#from control_msgs.msg import FollowJointTrajectoryActionGoal

#Seleccion de pata
print 'Seleccione lado (r o l)'
lado = raw_input()
print 'Seleccione numero de pata'
num = int(input())

global pos

def callback(data):
	#Damos la orientacion de cada articulacion en orden del cuerpo al pie
	#global pos
	if lado == 'r' and num == 1:
		print "Pos r1: (", data.position[9], data.position[15], data.position[21], data.position[3], ")"
		pos = data.position
	if lado == 'r' and num == 2:
		print "Pos r2: (", data.position[10], data.position[16], data.position[22], data.position[4], ")"
	if lado == 'r' and num == 3:
		print "Pos r3: (", data.position[11], data.position[17], data.position[23], data.position[5], ")"
	if lado == 'l' and num == 1:
		print "Pos l1: (", data.position[6], data.position[12], data.position[18], data.position[0], ")"
	if lado == 'l' and num == 2:
		print "Pos l2: (", data.position[7], data.position[13], data.position[19], data.position[1], ")"
	if lado == 'l' and num == 3:
		print "Pos l3: (", data.position[8], data.position[14], data.position[20], data.position[2], ")"
	#rospy.sleep(2)

def listener():
	rospy.init_node('robominer_joint_position_subscriber', anonymous=True)
	rospy.Subscriber("robominer/joint_states", JointState, callback, queue_size=1, buff_size=65536)   
	rospy.spin()

if __name__ == '__main__':
    listener()


