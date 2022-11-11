#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Test node is alive!")

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello, im still here :)")
        rate.sleep()
