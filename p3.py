# -*- coding: utf-8 -*-
"""

@author: Satyajit Mahunta
"""

import numpy as np
import cv2
import matplotlib. pyplot as plt

nadia = cv2.imread('Nadia_Murad.jpg',0)

plt.imshow(nadia, cmap='gray')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(img):
    
    face_img = img.copy()
    
    face_rect = face_cascade.detectMultiScale(face_img)
    
    for (x,y,w,h) in face_rect:
        cv2.rectangle(face_img,(x,y), (x+w,y+h),(255,0,0), 10)
    
    return face_img
img1 = detect_face(nadia)
plt.imshow(img1, cmap='gray')

def detect_face(img):
    
    face_img = img.copy()
    
    face_rect = face_cascade.detectMultiScale(face_img)
    
    for (x,y,w,h) in face_rect:
        cv2.rectangle(face_img,(x,y), (x+w,y+h),(255,0,0), 10)
    
    return face_img