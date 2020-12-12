import rospy
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import time

rospy.init_node('move_robot_back_and_forth')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
speed = 3

while not rospy.is_shutdown():
    for i in range(1000):
        print(vel_msg.angular)
        vel_msg.angular.z = -1 *  speed
        velocity_publisher.publish(vel_msg)
        time.sleep(1)
