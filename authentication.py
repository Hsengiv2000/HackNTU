# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:27:12 2019

@author: Venkatesh
"""

class Authentication:
    def __init__(self ,client ,userID  , PWD):
        self.uid = userID
        self.pwd = PWD
        self.client = client
    def Authenticate(self):
        if self.client == True:
            f = open("secrets.txt" , "w")
            if f!= None:
                f.writelines(self.uid + "\n")
                f.writelines(self.pwd)
                f.close()
                print("Account created Successfully")
                return True
        else:
            f  = open("secrets.txt" , "r")
            a =    f.readline()[0:-1]
            b = f.readline()
            print(b)
            if a == self.uid and b == self.pwd:
                print("Authenticated!")
                return True
            else:
                return False
