# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:24:39 2019

@author: Sudharshan
"""

import speech_recognition as sr
import storage
import time

def speechToText(sound):
    try:
        r = sr.Recognizer()
        with sound as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        raise sr.UnknownValueError("Sound file clarity too low, try again.")
    except FileNotFoundError:
        raise FileNotFoundError("Check your file source and try again!")

def readSound(filepath):
    try:
        return sr.AudioFile(filepath)
    except IOError:
        raise IOError("File not found")
    except FileNotFoundError:
        raise FileNotFoundError("Check your file input and try again!")

def storeText(text):
    words = str(text).split(" ")
    for word in words:
        storage.addWord(word)
    
def searchWord(word):
    return storage.getCount(word)

def countWordsInFile(sourcesound, word):
    sourcesound = readSound(sourcesound)
    text = speechToText(sourcesound)
    storeText(text)
    print(text + "\n")
    count = searchWord(word)
    storage.clearStorage()
    return count

def countWords(text, word):
    storeText(text)
    count = searchWord(word)
    storage.clearStorage()
    return count

def run(filepath):   
    #print(sr.__version__)
    r = sr.Recognizer()
    happy = sr.AudioFile(filepath)
    happy.DURATION == 10
    audioArray= []
    x= 0
    t= 10.0 
    prevt = 0.0
    with happy as source:
            
        #print("hi")
        #print(source.DURATION)
        x = source.DURATION
        audio = r.record(source, duration = t,offset=prevt)
   
        #print("hey")
        #print((audio))
    while(t<x):
        with happy as source:
            #print("waslsls")
            #print(t)
            audio=r.record(source, duration = t , offset = prevt)
            t+=10
            prevt+=10
            #print("supppu;ar")
            audioArray.append(audio)
    #print("sup")
    try:
        for audio in audioArray:
            a= r.recognize_google(audio)
        
            return a
            time.sleep(0.1)
    except:
        raise ("An error occurred.\n")
    


