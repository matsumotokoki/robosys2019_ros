#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import matplotlib.pyplot as plt

def cb(message):
    bridge = CvBridge()
    message = bridge.imgmsg_to_cv2(message)
    rospy.loginfo(message)
    print("-------------------\n")
    plt.title('recived image')
    plt.imshow(message[:,:,::-1])
    plt.pause(.01)
    plt.cla()

if __name__ == '__main__':
    rospy.init_node('recieve_img')
    sub = rospy.Subscriber('send_img', Image, cb)
    rospy.spin()
