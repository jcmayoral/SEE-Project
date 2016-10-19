# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:49:08 2016

@author: jose
"""

import cv2
import numpy as np

# From Matlab Instrinsic matrix
#1.0e+03 *
#    1.4607         0         0
#         0    1.4639         0
#    0.9609    0.5486    0.0010
intrinsic_matrix = 1000 * np.array(([1.4607,0,0],[0,1.4639,0],[0.9609,0.5486,0.0010]))

print intrinsic_matrix

cap = cv2.VideoCapture(0)
i = 0

flag = True

while(flag):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(0)
    print key
    cv2.imwrite('/home/jose/Documents/messigray.png',frame)
    i = i+1
    if key == 27:
        flag = False
     #   break
# When everything done, release the capture
"""
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        print x,y
        cropping = False
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("test", img)
  
cv2.namedWindow('test', cv2.WINDOW_NORMAL)
cv2.setMouseCallback("test", click_and_crop)
img = cv2.imread('test.png',0)

while(True):
    cv2.imshow('test',img)
    if(cv2.waitKey(0)==ord('g')):
        break
    
cv2.destroyAllWindows()
"""
cap.release()
cv2.destroyAllWindows()