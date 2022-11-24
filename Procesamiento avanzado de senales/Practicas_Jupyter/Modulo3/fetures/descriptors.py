#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:36:34 2019

@author: Gustavo
"""

import cv2
import numpy as np

img = cv2.cvtColor(cv2.imread('Unknown.png'), cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,127,255,0)
_, contours, _ = cv2.findContours(thresh, 1, 2)


cnt = contours[0]
M = cv2.moments(cnt)
print (M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt,True)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)


hull = cv2.convexHull(cnt)

k = cv2.isContourConvex(cnt)

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow('frame',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()




rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img,[box],0,(0,0,255),2)
cv2.imshow('frame',im)
cv2.waitKey(0)
cv2.destroyAllWindows()


(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),3)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()