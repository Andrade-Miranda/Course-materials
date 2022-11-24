#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:43:58 2019

@author: Gustavo
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


#### Laplacian
img = cv2.cvtColor(cv2.imread('moon.tif'),cv2.COLOR_BGR2GRAY)
kernel1 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])


#laplacian=abs(cv2.filter2D(img,CV_32F,kernel))
laplacian = cv2.Laplacian(img,cv2.CV_64F)
g=img-0.8*laplacian

plt.subplot(221),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(laplacian,cmap = 'gray'),plt.title('Laplacian Filter')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(g,cmap = 'gray'),plt.title('Sharped')
plt.xticks([]), plt.yticks([])
plt.show()


#####Generate Noise
import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise
from skimage.exposure import rescale_intensity


I = cv2.cvtColor(cv2.imread('lena.png'),cv2.COLOR_BGR2RGB); # 1/ -1: color mode; 0: gray mode
gauss = random_noise(I, mode='gaussian', seed=None, clip=True)
sp = random_noise(I, mode='s&p', seed=None, clip=True, salt_vs_pepper=0.4)

gaussint=rescale_intensity(gauss, out_range=(0, 255))
gaussint = gaussint.astype(np.uint8)
spint=rescale_intensity(sp, out_range=(0, 255))
spint = spint.astype(np.uint8)


dst0=cv2.medianBlur(I,5)
dst1=cv2.medianBlur(gaussint,5)
dst2=cv2.medianBlur(spint,5)



plt.subplot(231), plt.imshow(I,cmap='gray'), plt.title('Origin')
plt.subplot(232), plt.imshow(gauss,cmap='gray'), plt.title('Gaussian')
plt.subplot(233), plt.imshow(sp,cmap='gray'), plt.title('Salt & Pepper')
plt.subplot(234), plt.imshow(dst0,cmap='gray'), plt.title('Origin')
plt.subplot(235), plt.imshow(dst1,cmap='gray'), plt.title('Filter median - Gaussian Noise')
plt.subplot(236), plt.imshow(dst2,cmap='gray'), plt.title('Filter median - Salt and Pepper')
plt.show();