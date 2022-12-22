# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:02:59 2022

@author: samar
"""

import cv2 
import numpy as np 
img = cv2.imread('digitos-1.png', 0) 
kernel = np.ones((4,4), np.uint8) 
  
# img_erosion = cv2.erode(img, kernel, iterations=1) 
# img_dilation = cv2.dilate(img, kernel, iterations=1) 

# Abertura
def abertura(img,kernel,it_erode,it_dilate):
    img_etapa1 = cv2.erode(img, kernel, iterations=it_erode) 
    img_abertura = cv2.dilate(img_etapa1, kernel, iterations=it_dilate) 
    return img_abertura

#Fechamento
def fechamento(img,kernel,it_erode,it_dilate):
    img_etapa1 = cv2.dilate(img, kernel, iterations=it_dilate) 
    img_fechamento = cv2.erode(img_etapa1, kernel, iterations=it_erode) 
    return img_fechamento

img_out = cv2.erode(img, kernel, iterations=1)
img_out = fechamento(img_out,kernel,1,1)
img_out = abertura(img_out,kernel,2,1)
img_out = cv2.dilate(img_out, kernel, iterations=2)

cv2.imshow('saida', img_out) 
cv2.waitKey(0) 