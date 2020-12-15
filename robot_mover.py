import rospy
from geometry_msgs.msg import Twist
from math import pi
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math

class RobotMoving:
    def __init__(self, node_name):
        self._node_name = node_name
        rospy.init_node(self._node_name)
        self._velocity_subscriber = rospy.Subscriber ('/odometry/filtered', Odometry, self.__get_rotation)
        self._velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self._velocity_command = Twist()
        self._roll = 0
        self._pitch = 0
        self._yaw = -9999
        self._kp = 0.5
        self._rate = rospy.Rate(50)

    def __get_rotation (self, arg):
        orientation_q = arg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (self._roll, self._pitch, self._yaw) = euler_from_quaternion (orientation_list) 
        print(self.radians_to_degrees(self._yaw))

    def radians_to_degrees(self, rad):
        return rad * 180 / math.pi

    def rotation_in_place(self, desired_degree):
        """
        Rotate robot by specific angle
        """
        if desired_degree > 0:
            z_num = 1
        else:
            z_num = -1
        while not rospy.is_shutdown():
            current_degree = self.radians_to_degrees(self._yaw)
            print(round(current_degree))
            if desired_degree == int(round(current_degree)):
                print('Finish')
                break
            self._velocity_command.angular.z = 0.5
            self._velocity_publisher.publish(self._velocity_command)
            self._rate.sleep()

    def stright_line_drive(distance):
        pass

