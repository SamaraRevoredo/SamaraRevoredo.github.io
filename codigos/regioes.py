# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:18:27 2022

@author: samar
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('biel.png',cv2.IMREAD_GRAYSCALE)

x1 = input('Digite o limite lateral esquerdo: ')
x2 = input('Digite o limite lateral direito: ')
y1 = input('Digite o limite superior: ')
y2 = input('Digite o limite inferior: ')

for i in range(int(x1),int(x2)):
    for j in range(int(y1),int(y2)):
        img[i,j] = 255-img[i,j]

cv2.imshow('image',img)
cv2.waitKey()