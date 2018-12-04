# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:04:24 2018

@author: laksh
"""

import cv2

face_cascade = cv2.CascadeClassifier('E:\\A\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)   
count=0
while True:
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
    
        cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q') or count==150:
        break

cap.release()
cv2.destroyAllWindows()      