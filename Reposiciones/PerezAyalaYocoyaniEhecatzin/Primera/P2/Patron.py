# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 18:08:39 2018

@author: yocoy
"""

class Patron():
    
    def __init__(self):
        self.patron = []
        
    def lectorPatron(self):
        archivo = open("patron.txt","r")
        for x in archivo.readlines():
            print (x)
        archivo.close()