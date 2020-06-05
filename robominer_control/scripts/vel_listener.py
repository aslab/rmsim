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
			print "Vel r1: (", data.velocity[9], data.velocity[15], data.velocity[21], data.velocity[3], ")"
	if lado == 'r':
		if num == 2:
			print "Vel r2: (", data.velocity[10], data.velocity[16], data.velocity[22], data.velocity[4], ")"				
	if lado == 'r':
		if num == 3:
			print "Vel r3: (", data.velocity[11], data.velocity[17], data.velocity[23], data.velocity[5], ")"
	if lado == 'l':
		if num == 1:
			print "Vel l1: (", data.velocity[6], data.velocity[12], data.velocity[18], data.velocity[0], ")"				
	if lado == 'l':
		if num == 2:		
			print "Vel l2: (", data.velocity[7], data.velocity[13], data.velocity[19], data.velocity[1], ")"
	if lado == 'l':
		if num == 3:
			print "Vel l3: (", data.velocity[8], data.velocity[14], data.velocity[20], data.velocity[2], ")"
	#rospy.sleep(1)

def listener():
	rospy.init_node('robominer_joint_velocity_subscriber', anonymous=True)
	rospy.Subscriber("robominer/joint_states", JointState, callback, queue_size=1, buff_size=65536)   
	rospy.spin()

if __name__ == '__main__':
    listener()


