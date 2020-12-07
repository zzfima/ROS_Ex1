import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('move_robot')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
speed = 0.5

while not rospy.is_shutdown():
    for i in range(30):
        vel_msg.linear.x = speed
        velocity_publisher.publish(vel_msg)
        time.sleep(0.1)
    for i in range(30):
        vel_msg.linear.x = -1 * speed
        velocity_publisher.publish(vel_msg)
        time.sleep(0.1)
