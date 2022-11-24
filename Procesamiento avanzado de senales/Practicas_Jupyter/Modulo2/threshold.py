#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:31:21 2019

@author: Gustavo
"""

# import opencv 
import cv2 
import matplotlib.pyplot as plt


src = cv2.imread("lena.png",1); 
# Read image 
src = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE); 
cv2.imshow("original",src)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Basic threhold example 
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY); 
cv2.imshow("images1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-threshold-example.jpg", dst); 


# Thresholding with maxValue set to 128
th, dst = cv2.threshold(src, 127, 128, cv2.THRESH_BINARY); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-binary-maxval.jpg", dst); 



# Thresholding using THRESH_BINARY_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY_INV); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-binary-inv.jpg", dst); 

# Thresholding using THRESH_TRUNC 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC); 
cv2.imshow("images1",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-trunc.jpg", dst); 

# Thresholding using THRESH_TOZERO 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-tozero.jpg", dst); 

# Thresholding using THRESH_TOZERO_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV); 
cv2.imshow("images",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst); 

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
ret,thr = cv2.threshold(src, 0, 255,cv2.THRESH_OTSU)
cv2.imshow("images",thr)
cv2.waitKey(0)
cv2.destroyAllWindows()


####GUINEO###
imgray = cv2.imread("guineo.jpg");
b,g,r=cv2.split(imgray)
plt.hist(b.ravel(),256,[0,256]); plt.show()
cv2.imshow("Imagen",b)
cv2.waitKey(0)
cv2.destroyAllWindows()


####threslhold
ret, thresh2 = cv2.threshold(b, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("threshold",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()




#To draw all the contours in an image:
im2, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(imgray, contours, -1, (255,0,0), 3)
cv2.imshow("images",imgray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
##To draw an individual contour, say 4th contour:
#cv2.drawContours(imgray, contours, 3, (0,255,0), 3)
#cv2.imshow("images",imgray)
#cv2.waitKey(0)
##But most of the time, below method will be useful:
#cnt = contours[4]
#cv2.drawContours(imgray, [cnt], 0, (0,255,0), 3)







#### Histogram equalization
import cv2

equ = cv2.equalizeHist(src) 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(src)



hist = cv2.calcHist([src],[0],None,[256],[0,256])

img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()
   
    
    
    