#!/usr/bin/env python2
import rospy

from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge
import matplotlib.pyplot as plt

rospy.init_node('send')
pub = rospy.Publisher('send_img', Image, queue_size=1)
rate = rospy.Rate(10)
cap = cv2.VideoCapture(0)

bridge = CvBridge()
while not rospy.is_shutdown():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    cv2.imshow('Raw Frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
    pub.publish(msg)
    rate.sleep()
