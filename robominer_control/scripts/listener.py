#!/usr/bin/env python
import rospy
from geometry_msgs.msg import WrenchStamped
import math
import time

#Seleccion de pata
print 'Seleccione lado (r o l)'
lado = raw_input()
print 'Seleccione numero de pata'
num = int(input())
	
def callback(data,args):
	print args
	print 'Fuerza:', math.sqrt(data.wrench.force.x**2 + data.wrench.force.y**2 + data.wrench.force.z**2), 'N'
	print 'Par:', math.sqrt(data.wrench.torque.x**2 + data.wrench.torque.y**2 + data.wrench.torque.z**2), 'Nm'
	time.sleep(1)
	
	    
def listener():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# name are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('robominer_ft_sensor_listener', anonymous=True)
	
	
	
	if lado == 'r':
		if num == 1:
			rospy.Subscriber("/robominer/Rev3_r_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_r_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_r_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_r_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_r_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_r_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_r_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_r_1_ft_sensor_topic")
			time.sleep(.5)
			
	if lado == 'r':
		if num == 2:
			rospy.Subscriber("/robominer/Rev3_r_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_r_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_r_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_r_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_r_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_r_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_r_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_r_2_ft_sensor_topic")
			time.sleep(.5)
					
	if lado == 'r':
		if num == 3:
			rospy.Subscriber("/robominer/Rev3_r_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_r_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_r_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_r_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_r_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_r_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_r_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_r_3_ft_sensor_topic")
			time.sleep(.5)
			
	if lado == 'l':
		if num == 1:
			rospy.Subscriber("/robominer/Rev3_l_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_l_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_l_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_l_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_l_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_l_1_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_l_1_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_l_1_ft_sensor_topic")
			time.sleep(.5)
							
	if lado == 'l':
		if num == 2:			
			#Pata l2
			rospy.Subscriber("/robominer/Rev3_l_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_l_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_l_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_l_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_l_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_l_2_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_l_2_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_l_2_ft_sensor_topic")
			time.sleep(.5)
			
	if lado == 'l':
		if num == 3:
			#Pata l3
			rospy.Subscriber("/robominer/Rev3_l_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev3_l_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev5_l_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev5_l_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev8_l_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev8_l_3_ft_sensor_topic")
			time.sleep(.5)
			rospy.Subscriber("/robominer/Rev11_l_3_ft_sensor_topic", WrenchStamped, callback, "/robominer/Rev11_l_3_ft_sensor_topic")
			time.sleep(.5)
	

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
    listener()
