#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
base = BaseOverlay("base.bit")
#Mode = VideoMode(1920,1080,60)
Mode = VideoMode(640,480,24)
frame_in_width = 640
frame_in_height = 480
#frame_in_width = 1920
#frame_in_height = 1080

import os
os.environ["OPENCV_LOG_LEVEL"]="SILENT"
# initialize camera from OpenCV
import cv2

videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, frame_in_width);
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_in_height);

print("Capture device is open: " + str(videoIn.isOpened()))

import numpy as np
ret,frame_vga = videoIn.read()
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
plt.imshow(frame_vga[:,:,[2,1,0]])
plt.show()

