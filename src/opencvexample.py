#!/usr/bin/env python
import cv2
import urllib 
import numpy as np
import math

def get_from_webcam():
    stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
    bytes=''
    bytes+=stream.read(32384)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        return i

def get_from_file(filename):
    return cv2.imread(filename)



print "loading from file"
image = get_from_file('/home/ubuntu/catkin_ws/test.jpg')
cv2.imshow('test',image)

key = cv2.waitKey(0)
if key == 27:
    exit(0)  