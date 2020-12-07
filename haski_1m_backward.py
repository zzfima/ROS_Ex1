import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time

x_position = 0
initial_x_position = 0

def odometry_callback(msg):
    """
    callback new message arrived
    """
    global x_position
    x_position = msg.pose.pose.position.x

rospy.init_node('move_one_meter')
rospy.Subscriber('/odometry/filtered', Odometry, odometry_callback)
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
speed = 0.5

while initial_x_position == 0:
    print('waiting for initial position')
    initial_x_position = x_position
    time.sleep(0.1)

while not rospy.is_shutdown():
    while abs(x_position - initial_x_position) < 1:
        vel_msg.linear.x = -1 * speed
        print(abs(x_position - initial_x_position))
        velocity_publisher.publish(vel_msg)
        time.sleep(0.1)
    break
