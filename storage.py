# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:57:06 2019

@author: Sudharshan
"""

words = {}

def addWord(word):
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

def getCount(word):
    try:
        return words[word]
    except KeyError:
        return 0
    
def clearStorage():
    global words
    words = {}
    
