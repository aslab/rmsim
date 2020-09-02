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

def callback(data):
	#Damos la orientacion de cada articulacion en orden del cuerpo al pie
	if lado == 'r':
		if num == 1:
			print "Par r1: (", data.effort[9], data.effort[15], data.effort[21], data.effort[3], ")"
	if lado == 'r':
		if num == 2:
			print "Par r2: (", data.effort[10], data.effort[16], data.effort[22], data.effort[4], ")"				
	if lado == 'r':
		if num == 3:
			print "Par r3: (", data.effort[11], data.effort[17], data.effort[23], data.effort[5], ")"
	if lado == 'l':
		if num == 1:
			print "Par l1: (", data.effort[6], data.effort[12], data.effort[18], data.effort[0], ")"				
	if lado == 'l':
		if num == 2:		
			print "Par l2: (", data.effort[7], data.effort[13], data.effort[19], data.effort[1], ")"
	if lado == 'l':
		if num == 3:
			print "Par l3: (", data.effort[8], data.effort[14], data.effort[20], data.effort[2], ")"
	#rospy.sleep(1)

def listener():
	rospy.init_node('robominer_joint_effort_subscriber', anonymous=True)
	rospy.Subscriber("robominer/joint_states", JointState, callback, queue_size=1, buff_size=65536)   
	rospy.spin()

if __name__ == '__main__':
    listener()


