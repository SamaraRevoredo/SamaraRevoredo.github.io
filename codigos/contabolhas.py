# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:43:06 2022

@author: samar
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2
from skimage.segmentation import flood, flood_fill
img = cv2.imread('bolhas.png',cv2.IMREAD_GRAYSCALE)

cols,rows = img.shape
print(img[0,0])
for i in range(0,cols):
    img[i,0] = 255
    img[i,rows-1] = 255
for i in range(0,rows):
    img[0,i] = 255
    img[cols-1,i] = 255

img = flood_fill(img, (0,0), 0)
img = flood_fill(img,(0,0),30)
num_obj = 0
for i in range(0,rows):
    for j in range(0,cols):
        if img[i,j] == 255:
            num_obj += 1
            img = flood_fill(img,(i, j),200)

print('numero total de objetos = ',num_obj)
com_furo = 0
for i in range(0,rows):
    for j in range(0, cols):
        if img[i,j] == 0:
                img = flood_fill(img,(i,j),200)
                com_furo += 1
print('Total de objetos com furo: ',com_furo)       
cv2.imshow('image',img)
cv2.waitKey()