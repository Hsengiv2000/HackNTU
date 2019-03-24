# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:55:31 2017

@author: Venkatesh
"""

import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model

print(cv2.__version__)
class Predicter:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detection_model_path = 'haarcascade_frontalface_default.xml'
        self.emotion_model_path = '_mini_XCEPTION.102-0.66.hdf5'
        self.recognizer.read('trainner/trainner.yml')
        self.cascadePath = r"C:\Users\Venkatesh\Documents\cascadesPython\haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath);
        self.emotion_classifier = load_model(self.emotion_model_path, compile=False)
        self.EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
     "neutral"]

        self.cam = cv2.VideoCapture(0)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
    def run(self):
        while True:
            ret, im =self.cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=self.faceCascade.detectMultiScale(gray, 1.2,5)
            
            canvas = np.zeros((250, 300, 3), dtype="uint8")
            frameClone = im.copy()
            for(x,y,w,h) in faces:
                roi = gray[y:y + h, x:x + w]
                roi = cv2.resize(roi, (64, 64))
                roi = roi.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                preds = self.emotion_classifier.predict(roi)[0]
               
                self.emotion_probability = np.max(preds)
                label = self.EMOTIONS[preds.argmax()]
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = self.recognizer.predict(gray[y:y+h,x:x+w])
                preds[0]+=preds[1]
                preds[1] = 0
                np.delete(preds, 1)
                preds[4]+=preds[2]
                preds[2] = 0
                for (i, (emotion, prob)) in enumerate(zip(self.EMOTIONS, preds)):
                        # construct the label text
                        text = "{}: {:.2f}%".format(emotion, prob * 100)
                        print("preds :" , preds)
                        # draw the label + proqbability bar on the canvas
                       # emoji_face = feelings_faces[np.argmax(preds)]
        
                        
                        w = int(prob * 300)
                        cv2.rectangle(im, (7, (i * 35) + 5),
                        (w, (i * 35) + 35), (0, 0, 255), -1)
                        cv2.putText(im, text, (10, (i * 35) + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                        (255, 255, 255), 2)
                        
                        cv2.putText(im, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2),
                        '''
                       # cv2.putText(im, "Score : " , (x, y - 10),
                        #cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                        cv2.rectangle(im, (x, y), (x + w, y + h),
                                      (0, 0, 255), 2)
                       # cv2.imshow('your_face', im)
                        '''
                        
                print("confidence is : " , conf)
                if(conf>40):
                    Id = Id
                     
                else:
                    Id="Unknown"
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
                print(str(Id))
                
            cv2.imshow("Probabilities", im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
           # cv2.imshow('recognizer',im) 
            #if cv2.waitKey(20) & 0xFF==ord('q'):
             #   break
        self.cam.release()
        cv2.destroyAllWindows()
        

          
'''
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
         
        print("confidence is : " , conf)
        if(conf>40):
            if(Id==1):
                Id="Rahul"
            elif(Id==2):
                Id="yang peng"
            elif Id==3:
                Id="Matt"
            elif Id==4:
                Id ="Uggi"
            elif Id==5:
                Id = "Sundar"
                     
        else:
            Id="Unknown"
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        print(str(Id))
            # cv2.PutText(im, str(Id), (x, y+h) , font, 1 , (0,255,0) )
    cv2.imshow('recognizer',im) 
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
'''