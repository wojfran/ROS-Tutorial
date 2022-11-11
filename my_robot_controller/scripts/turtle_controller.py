#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from random import randrange

previous_y = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose: Pose):
    cmd = Twist()
    if pose.x > 9 or pose.x < 2 or pose.y > 9 or pose.y < 2:
        cmd.linear.x = 1
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = -0.5
    pub.publish(cmd)

    global previous_y
    if pose.y >= 4.5 and previous_y < 4.5:
        previous_y = pose.y
        call_set_pen_service(255, 0, 0, 5, 0)
    elif pose.y < 4.5 and previous_y >= 4.5:
        call_set_pen_service(0, 0, 255, 5, 0)
    previous_y = pose.y

if __name__ == '__main__':
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")
    call_set_pen_service(255, 0, 0, 4, 0)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Node started")

    rospy.spin()