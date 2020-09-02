#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import WrenchStamped

def callbackr1(data,args):
	try:
		print data.position[3]
	except:
		print 'Oh sielos, no hay', args, '!' 
def callbackr2(data,args):
	try:
		print data.position[4]
	except:
		print 'Oh sielos, no hay', args, '!' 
def callbackr3(data,args):
	try:
		print data.position[5]
	except:
		print 'Oh sielos, no hay', args, '!' 
def callbackl1(data,args):
	try:
		print data.position[0]
	except:
		print 'Oh sielos, no hay', args, '!' 
def callbackl2(data,args):
	try:
		print data.position[1]
	except:
		print 'Oh sielos, no hay', args, '!' 
def callbackl3(data,args):
	try:
		print data.wrench.force.x
	except:
		print 'Oh sielos, no hay', args, '!' 
		

def listener():	
	
	rospy.init_node('robominer_patas_listener', anonymous=True)

	#rospy.Subscriber("robominer/joint_states", JointState, callbackr1, "pata r1") 
	#rospy.Subscriber("robominer/joint_states", JointState, callbackr2, "pata r2") 
	#rospy.Subscriber("robominer/joint_states", JointState, callbackr3, "pata r3") 
	#rospy.Subscriber("robominer/joint_states", JointState, callbackl1, "pata l1") 
	#rospy.Subscriber("robominer/joint_states", JointState, callbackl2, "pata l2") 
	rospy.Subscriber("/robominer/Rev3_l_3_ft_sensor_topic", WrenchStamped, callbackl3, "pata l3") 
		
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
		
if __name__ == '__main__':
    listener()