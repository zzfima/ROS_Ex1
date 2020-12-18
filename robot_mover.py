import rospy
from geometry_msgs.msg import Twist
from math import pi
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import math
import time

class RobotMoving:
    def __init__(self, node_name):
        self._node_name = node_name
        rospy.init_node(self._node_name)
        self._velocity_subscriber = rospy.Subscriber ('/odometry/filtered', Odometry, self.__get_rotation)
        self._velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self._velocity_command = Twist()
        self._current_degree = -9999
        print('init position')
        # polling odometer
        while(self._current_degree == -9999):
            time.sleep(0.1)
        self._rate = rospy.Rate(100)

    def __get_rotation (self, arg):
        orientation_q = arg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion (orientation_list) 
        self._current_degree = self.__convert_to_normal_degrees(yaw)
        print(self._current_degree)

    def __convert_to_normal_degrees(self, rad):
        """
        return degrees 0-360 (0/360 - left, 90 - down, 180 - right, 270 up)
        """

        '''
                    current degrees: 
                -45      -90     -135 
                   .      |     . 
                      .   |   .
                        . | .
            0 <---------------------> 180/-180
                        . | .
                      .   |    .
                    .     |       . 
                 45      90        135
        so, add 360 to make it positive only, so it will 0, 90, 180, ...360
        '''        
        deg = self.__radians_to_degrees(rad)    
        if deg < 0: 
            deg += 360
        return deg
        
    def __radians_to_degrees(self, rad):
        return rad * 180 / math.pi

    def rotation_in_place(self, desired_degree):
        """
        Rotate robot by specific angle
        """
        if desired_degree > self._current_degree:
            z_num = 0.3
        else:
            z_num = -0.3
        while not rospy.is_shutdown():
            rounded_current_degree = int((round(self._current_degree)))
            if desired_degree == rounded_current_degree:
                print('Finish')
                break
            self._velocity_command.angular.z = z_num
            self._velocity_publisher.publish(self._velocity_command)
            self._rate.sleep()

    def stright_line_drive(distance):
        pass

