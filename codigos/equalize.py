# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:55:49 2022

@author: samar
"""

import cv2
from copy import copy
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('biel.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey()
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
hist_acum = []
hist_acum.append(int(hist[0]))
for i in hist[1:]:
    hist_acum.append(hist_acum[len(hist_acum)-1]+int(i))
cols,rows = img.shape
for i in range(0,rows):
    for j in range(0,cols):
        img[i,j] = np.round(hist_acum[img[i,j]]*255/(rows*cols))

hist_eq = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist_eq)
plt.show()
cv2.imshow('image',img)
cv2.waitKey()

