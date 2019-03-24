# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:54:35 2017

@author: Venkatesh
"""

import cv2
import numpy as np
class FaceCropper2:
    def __init__(self,Id,name,length ):
        self.samplenum = 1
        self.length = int(length)
        self.Id = int(Id)
        self.name = name
        self.cam =cv2.VideoCapture(0)
        self.detector  = cv2.CascadeClassifier(r'C:\Users\Venkatesh\Documents\cascadesPython\haarcascade_frontalface_default.xml')
    def run(self):
        
        while(True):
                ret = False
                img = []
                img = cv2.imread(self.name +  str(self.samplenum)+".jpg")
                if img!=[]:
                    ret = True
                if ret:
                    print (ret)
                    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
                    faces = self.detector.detectMultiScale(gray, 1.3 , 5)
    
                    for(x , y , w, h ) in faces:
                        cv2.rectangle(img , (x,y) , (x+w,  y +h), (255,0,0), 2)
                        self.samplenum+=1
                        #the folder was read only, hence wouldnt work
                    isit = cv2.imwrite(r"C:\Users\Venkatesh\Documents\python projects\MOONJI\data\User."+str(self.Id)+'.'+str(self.samplenum)+".bmp" , gray)
                    print (isit)
                    cv2.imshow('trainer' , img)
                        
                    key = cv2.waitKey(5) 
                    if  key ==27 or self.samplenum >self.length:
                        break
                    
                            
        self.cam.release()
        
        cv2.destroyAllWindows()
        
FC = FaceCropper2("44" , "pichai" , 11)
FC.run()
