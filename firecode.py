# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:27:48 2019

@author: sidha
"""
from firebase import firebase
firebase = firebase.FirebaseApplication('https://justforfun-2cba8.firebaseio.com/')
def readfile():
    print("getting yml data from firebase")
    res = firebase.get('-LagVaOwPzoKOgjltW5h/1', None)
    f1 = open("trainner.yml", 'w')
    for i in res:
        f1.write(i)    
    f1.close()
    
def writefile():
    f = open('trainner.yml', 'r')
    s = f.readlines()
    print("writing to firebase")
    firebase.post('/', {1:s})
    print("wrote to firebase")
    f.close()
    
    
#f = open('legitone.yml', 'r')
#s = f.readlines()
#s1 = s[0:len(s)/2]
#s2 = s[len(s)/2:]
#firebase.post('/', {2:s1})
#firebase.post('/', {3:s2})

#firebase.delete('/', '')
#firebase.post('/', {3:s2})


#def upload(f):
#    global counter
#    counter+=1
#    s = f.readlines()
#    firebase.post('/', {counter:s})
#        
#    
    


#def splitfiles():
#    lines_per_file = 30000
#    smallfile = None
#    with open('trainner.yml') as bigfile:
#        for lineno, line in enumerate(bigfile):
#            if lineno % lines_per_file == 0:
#                if smallfile:
#                    smallfile.close()
#                small_filename = 'small_file_{}.yml'.format(lineno)
#                smallfile = open(small_filename, "w")
#            smallfile.write(line)
#        
        
        
#        if smallfile:
#            smallfile.close()
#import os

#def openfile():
#    path = r'C:\Users\sidha\Anaconda3\Lib\site-packages\numpy\core'
#    for data_file in sorted(os.listdir(path)):
#        if( 'small_file' in data_file):
#            f = open(data_file, 'r')
#            upload(f)
#            
#            
            
            
            
    
#openfile()
        
        
        
#splitfiles()

#def combinefiles():
#    newline = "\r\n"
#    files = []
#    for i in range(0,2):
#        files[i] = "t" + str(i)
#    
#    outfile = "Output.txt"
#
#    for i in range(0, len(files)):
#        files[i] = open(files[i], "rU")
#
#    with open(outfile, "w") as out:
#      while True:
#        finished = True
#        for f in files:
#          line = f.readline()
#          if line != "":
#            finished = False
#            line = line.replace("\n", "")
#            out.write(line + newline)
#        if finished:
#          break
#combinefiles()

        

    
    
    
