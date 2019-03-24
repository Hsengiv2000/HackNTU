# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:28:38 2019

@author: Sudharshan
"""

from firebase import firebase

def getData(base):
    return base.get("/", None)

def getBase():
    base = firebase.FirebaseApplication(
            "https://hack-d78ce.firebaseio.com/")
    return base

def authenticate(username, password):
    try:
        base = getBase()
        count = 0
        #username, password = "", ""
        while count < 1:
            count += 1
            #username = inp.getNext("Enter username\n")
            dataset = getData(base)
            usernameExists = False
            for i in dataset:
                for j in dataset[i]:
                    if j == username:
                        usernameExists = True
          #              password = inp.getNext("Enter password.\n")
                        if password == dataset[i][j]:
                            print("Login Successful")
                            return True
                        else:
                            print("Incorrect password!\n")
                            #print("You have " + str(3 - count)
                                #+ " tries/try left.")
            if not usernameExists:
                print("Username doesn't exist")
                #print("You have " + str(3 - count)
                                #+ " tries/try left.")
                continue
        return False
    except TypeError:
        raise TypeError("Database is empty.")
    
def writeData(username , password):
#    username = inp.getNext("Enter a username to register with.\n")
    base = getBase()
    data = getData(base)
    _type = (str(type(data))[8:-2])
    if _type == 'NoneType':
        base.post("/", {username : password})
    else:
        contains = False
        for i in data:
            check = True
            for j in data[i]:
                if j == username:
                    print("Username already exists! Try again.\n")
                    check = False
            if not check:
                contains = True
                break
        if not contains:
            base.post("/", {username : password})
                
                    
         
        