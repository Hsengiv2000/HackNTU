# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:54:35 2017

@author: Venkatesh
"""

import cv2
import numpy as np


Id = input('Enter your ID ' )
print ('opening cam')
cam =cv2.VideoCapture(0)
detector  = cv2.CascadeClassifier(r'C:\Users\Venkatesh\Documents\cascadesPython\haarcascade_frontalface_default.xml')

sampleNum = 0
while(True):
    cam.open(0)
    if(cam.isOpened()):
        print ('camera is open')
        ret , img  = cam.read()
        if ret is True:
            print (ret)
            gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3 , 5)
            for(x , y , w, h ) in faces:
                cv2.rectangle(img , (x,y) , (x+w,  y +h), (255,0,0), 2)
                sampleNum = sampleNum +1
                #the folder was read only, hence wouldnt work
                isit = cv2.imwrite(r"C:\Users\Venkatesh\Documents\python projects\MOONJI\data\User."+str(Id)+'.'+str(sampleNum)+".bmp" , gray)
                print (isit)
                cv2.imshow('trainer' , img)
                
            key = cv2.waitKey(0) 
            if  key ==27:
                break
            elif sampleNum>50:
                break
            
cam.release()
cv2.destroyAllWindows()
    