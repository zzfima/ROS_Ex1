import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('move_robot_back_and_forth')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
speed = 0.5

while not rospy.is_shutdown():
    for i in range(30):
        vel_msg.linear.x = speed
        # vel_msg.angular.z = speed
        velocity_publisher.publish(vel_msg)
        time.sleep(0.1)
    for i in range(30):
        vel_msg.linear.x = -1 * speed
        # vel_msg.angular.z = -1 *  speed
        velocity_publisher.publish(vel_msg)
        time.sleep(0.1)
