#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from math import pi

def talker():
	pub =[ 
			#Pata r1
		[rospy.Publisher('/robominer/Rev3_r_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_1_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_r_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_1_position_controller/command', Float64, queue_size=10)],
			#Pata r2        
		[rospy.Publisher('/robominer/Rev3_r_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_2_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_r_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_2_position_controller/command', Float64, queue_size=10)],
			#Pata r3                
		[rospy.Publisher('/robominer/Rev3_r_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_r_3_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_r_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_r_3_position_controller/command', Float64, queue_size=10)],
			#Pata l1                
		[rospy.Publisher('/robominer/Rev3_l_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_1_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_l_1_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_1_position_controller/command', Float64, queue_size=10)],
			#Pata l2                
		[rospy.Publisher('/robominer/Rev3_l_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_2_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_l_2_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_2_position_controller/command', Float64, queue_size=10)],
			#Pata l3                
		[rospy.Publisher('/robominer/Rev3_l_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev5_l_3_position_controller/command', Float64, queue_size=10), 
		rospy.Publisher('/robominer/Rev8_l_3_position_controller/command', Float64, queue_size=10), rospy.Publisher('/robominer/Rev11_l_3_position_controller/command', Float64, queue_size=10)],

	]

	rospy.init_node('robominer_joint_command_talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	i = 0
	j = 0
	k = 0
	
	
	while not rospy.is_shutdown():
		#por algun motivo desconocido tiene que correr dos veces para que el robot se ponga en pie...
		while i  < 30:
			pos = [
				#Pata r1
				[pi/4, -pi/4, pi/2, pi/4],
				#Pata r2
				[0, -pi/4, pi/2, pi/4],
				#Pata r3
				[-pi/4, -pi/4, pi/2, pi/4],
				#Pata l1
				[-pi/4, -pi/4, pi/2, pi/4],
				#Pata l2
				[0, -pi/4, pi/2, pi/4],
				#Pata l3
				[pi/4, -pi/4, pi/2, pi/4]
			]

			#        pos = [
					#Pata r1
			#            [0, 0, 0, pi],
					#Pata r2
			#            [0, 0, 0, pi/2],
					#Pata r3
			#            [0, 0, 0, pi/2],
					#Pata l1
			#            [0, 0, 0, pi/2],
					#Pata l2
			#            [0, 0, 0, pi/2],
					#Pata l3
			#            [0, 0, 0, pi/2]
			#        ]

			rospy.loginfo(pos)
			#Pata r1
			pub[0][0].publish(pos[0][0])
			pub[0][1].publish(pos[0][1])
			pub[0][2].publish(pos[0][2])
			pub[0][3].publish(pos[0][3])
			#Pata r2
			pub[1][0].publish(pos[1][0])
			pub[1][1].publish(pos[1][1])
			pub[1][2].publish(pos[1][2])
			pub[1][3].publish(pos[1][3])
			#Pata r3
			pub[2][0].publish(pos[2][0])
			pub[2][1].publish(pos[2][1])
			pub[2][2].publish(pos[2][2])
			pub[2][3].publish(pos[2][3])
			#Pata l1
			pub[3][0].publish(pos[3][0])
			pub[3][1].publish(pos[3][1])
			pub[3][2].publish(pos[3][2])
			pub[3][3].publish(pos[3][3])
			#Pata l2
			pub[4][0].publish(pos[4][0])
			pub[4][1].publish(pos[4][1])
			pub[4][2].publish(pos[4][2])
			pub[4][3].publish(pos[4][3])
			#Pata l3
			pub[5][0].publish(pos[5][0])
			pub[5][1].publish(pos[5][1])
			pub[5][2].publish(pos[5][2])
			pub[5][3].publish(pos[5][3])

			rate.sleep()
			i = i + 1
			
		while j  < 10:
			#pos = [
				#Pata r1
			#	[pi/4, -pi/4, pi/4, 0],
				#Pata r2
			#	[0, -pi/4, pi/4, 0],
				#Pata r3
			#	[-pi/4, -pi/4, pi/4, 0],
				#Pata l1
			#	[-pi/4, -pi/4, pi/4, 0],
				#Pata l2
			#	[0, -pi/4, pi/4, 0],
				#Pata l3
			#	[pi/4, -pi/4, pi/4, 0]
			#]

			pos = [
				#Pata r1
				[pi/4, 0, pi/2, 0],
				#Pata r2
				[0, 0, pi/2, 0],
				#Pata r3
				[-pi/4, 0, pi/2, 0],
				#Pata l1
				[-pi/4, 0, pi/2, 0],
				#Pata l2
				[0, 0, pi/2, 0],
				#Pata l3
				[pi/4, 0, pi/2, 0]
			]


			#        pos = [
					#Pata r1
			#            [0, 0, 0, pi],
					#Pata r2
			#            [0, 0, 0, pi/2],
					#Pata r3
			#            [0, 0, 0, pi/2],
					#Pata l1
			#            [0, 0, 0, pi/2],
					#Pata l2
			#            [0, 0, 0, pi/2],
					#Pata l3
			#            [0, 0, 0, pi/2]
			#        ]

			rospy.loginfo(pos)
			#Pata r1
			pub[0][0].publish(pos[0][0])
			pub[0][1].publish(pos[0][1])
			pub[0][2].publish(pos[0][2])
			pub[0][3].publish(pos[0][3])
			#Pata r2
			pub[1][0].publish(pos[1][0])
			pub[1][1].publish(pos[1][1])
			pub[1][2].publish(pos[1][2])
			pub[1][3].publish(pos[1][3])
			#Pata r3
			pub[2][0].publish(pos[2][0])
			pub[2][1].publish(pos[2][1])
			pub[2][2].publish(pos[2][2])
			pub[2][3].publish(pos[2][3])
			#Pata l1
			pub[3][0].publish(pos[3][0])
			pub[3][1].publish(pos[3][1])
			pub[3][2].publish(pos[3][2])
			pub[3][3].publish(pos[3][3])
			#Pata l2
			pub[4][0].publish(pos[4][0])
			pub[4][1].publish(pos[4][1])
			pub[4][2].publish(pos[4][2])
			pub[4][3].publish(pos[4][3])
			#Pata l3
			pub[5][0].publish(pos[5][0])
			pub[5][1].publish(pos[5][1])
			pub[5][2].publish(pos[5][2])
			pub[5][3].publish(pos[5][3])

			rate.sleep()
			j = j + 1
			
			
		while k  < 10:
			pos = [
				#Pata r1
				[pi/4, pi/4, pi/4, 0],
				#Pata r2
				[0, pi/4, pi/4, 0],
				#Pata r3
				[-pi/4, pi/4, pi/4, 0],
				#Pata l1
				[-pi/4, pi/4, pi/4, 0],
				#Pata l2
				[0, pi/4, pi/4, 0],
				#Pata l3
				[pi/4, pi/4, pi/4, 0]
			]


			#        pos = [
					#Pata r1
			#            [0, 0, 0, pi],
					#Pata r2
			#            [0, 0, 0, pi/2],
					#Pata r3
			#            [0, 0, 0, pi/2],
					#Pata l1
			#            [0, 0, 0, pi/2],
					#Pata l2
			#            [0, 0, 0, pi/2],
					#Pata l3
			#            [0, 0, 0, pi/2]
			#        ]

			rospy.loginfo(pos)
			#Pata r1
			pub[0][0].publish(pos[0][0])
			pub[0][1].publish(pos[0][1])
			pub[0][2].publish(pos[0][2])
			pub[0][3].publish(pos[0][3])
			#Pata r2
			pub[1][0].publish(pos[1][0])
			pub[1][1].publish(pos[1][1])
			pub[1][2].publish(pos[1][2])
			pub[1][3].publish(pos[1][3])
			#Pata r3
			pub[2][0].publish(pos[2][0])
			pub[2][1].publish(pos[2][1])
			pub[2][2].publish(pos[2][2])
			pub[2][3].publish(pos[2][3])
			#Pata l1
			pub[3][0].publish(pos[3][0])
			pub[3][1].publish(pos[3][1])
			pub[3][2].publish(pos[3][2])
			pub[3][3].publish(pos[3][3])
			#Pata l2
			pub[4][0].publish(pos[4][0])
			pub[4][1].publish(pos[4][1])
			pub[4][2].publish(pos[4][2])
			pub[4][3].publish(pos[4][3])
			#Pata l3
			pub[5][0].publish(pos[5][0])
			pub[5][1].publish(pos[5][1])
			pub[5][2].publish(pos[5][2])
			pub[5][3].publish(pos[5][3])

			rate.sleep()
			k = k + 1
			
		break

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
