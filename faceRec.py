# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:49:13 2018

@author: Abhishek
"""
import os
import cv2
import urllib
import numpy as np

url='http://192.168.201.2:8080/shot.jpg'

def assurePath(path):
    dir=os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(dir)


def face_rec():
    
    model=cv2.face.LBPHFaceRecognizer_create()
    assurePath("C://Users//Abhishek//trainer//")
    model.read("C://Users//Abhishek//trainer//trainer1.yml")
    font =cv2.FONT_HERSHEY_SIMPLEX
    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    l=list()
    while(True):
        imgResponse = urllib.request.urlopen(url)
 
        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
 
        # Decode the array to OpenCV usable format
        img = cv2.imdecode(imgNp,-1)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x-20,y-20),(x+w+20,y+w+20),(0,255,0),2)
            id,confidence = model.predict(gray[y:y+h,x:x+w])
            l.append(id)
            cv2.rectangle(img,(x-22,y-90),(x+w+22,y-22),(0,255,0),-1)
            cv2.putText(img,str(id)+" : "+str(confidence),(x,y-40),font,1,(255,255,255),3)
        cv2.imshow("camera",img)
        if cv2.waitKey(10)& 0xff ==ord("q"):
                break
    cv2.destroyAllWindows()
    print(l)
        
if __name__=="__main__":
    face_rec()
            