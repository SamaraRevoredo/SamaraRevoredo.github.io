# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Samara R. S.
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('biel.png',cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape
for i in range(0,rows):
    for j in range(0,cols):
        img[i,j] = 255-img[i,j]
cv2.imshow('image',img)
cv2.waitKey()



