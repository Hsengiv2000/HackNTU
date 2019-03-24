# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:59:04 2017

@author: Venkatesh
"""

import cv2,os

import numpy as np
from PIL import Image
class Trainner:
    def __init__(self):
        self.detector= cv2.CascadeClassifier(r"C:\Users\Venkatesh\Documents\cascadesPython\haarcascade_frontalface_default.xml");
        


    def getImagesAndLabels(self, path):
    #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #create empth face list
        faceSamples=[]
    #create empty ID list
        Ids=[]
    #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
        #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath)
        #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
            try:
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
            except ValueError:
                print("hi")
            
        # extract the face from the training image sample
            print("lol")
            faces=self.detector.detectMultiScale(imageNp)
            print(123)
        #If a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids
    def run(self):
        faces,Ids = self.getImagesAndLabels(r'C:\Users\Venkatesh\Documents\python projects\MOONJI\data')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(Ids))
        recognizer.save('trainner/trainner.yml')

    
