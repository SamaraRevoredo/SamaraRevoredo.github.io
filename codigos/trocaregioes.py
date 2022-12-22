# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:53:47 2022

@author: samar
"""
# Observacao: para esse codigo funcionar a imagem precisa ser quadrada
import numpy as np
from matplotlib import pyplot as plt
import cv2
img = cv2.imread('biel.png',cv2.IMREAD_GRAYSCALE)
MAX,MAX2 = img.shape
aux = img.copy()
# A to D
for i in range(0,int(MAX/2)):
    for j in range(0,int(MAX/2)):
        aux[int(i+(MAX/2)),int(j+(MAX/2))] = img[i,j]
# B to C
for i in range(0,int(MAX/2)):
    for j in range(int(MAX/2),MAX):
        aux[int(i-(MAX/2)),int(j-(MAX/2))] = img[i,j]
# D to A
for i in range(int(MAX/2),MAX):
    for j in range(int(MAX/2),MAX):
        aux[int(i-(MAX/2)),int(j-(MAX/2))] = img[i,j]
# C to B
for i in range(int(MAX/2),MAX):
    for j in range(0,int(MAX/2)):
        aux[int(i-(MAX/2)),int(j-(MAX/2))] = img[i,j]

cv2.imshow('image',img)
cv2.waitKey()
cv2.imshow('image',aux)
cv2.waitKey()
