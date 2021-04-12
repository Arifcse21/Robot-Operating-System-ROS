#!/usr/bin/python

import sys, select, tty, termios
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
	key_pub = rospy.Publisher('keys', String, queue_size=1)		# Publisher type
	rospy.init_node('keyboard_driver')		# initialize the node keyboard_driver
	rate = rospy.Rate(10)					# 10Khz
	
	# save old terminal attributes
	old_attr =  termios.tcgetattr(sys.stdin)
	
	# receive input characcters when they are pressed
	tty.setcbreak(sys.stdin.fileno())
	
	
	print("Publishing keystrokes....")
	while not rospy.is_shutdown():
		if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
			key_pub.publish(sys.stdin.read(1))
		rate.sleep()

	# reset terminal attributes when done
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
 
	
	 
