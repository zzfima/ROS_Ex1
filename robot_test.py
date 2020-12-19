from robot_moving import RobotMoving
import rospy
import time

robot_moving = RobotMoving(node_name = 'circle_moving')
print('Go to 180')
robot_moving.rotation_in_place(180)
print('Go forward 1')
robot_moving.move_forvard(1)
