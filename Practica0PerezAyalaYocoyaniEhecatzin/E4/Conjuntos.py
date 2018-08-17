# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 18:55:57 2018

@author: yocoy
"""

class Conjuntos:
    
    def __init__(self,conjunto, valMin, valMax):
        self.conjunto = conjunto
        self.valMin = valMin
        self.valMax = valMax
        self.c1 = []
        self.c2 = []
        self.c3 = []
        self.c4 = []
        
    def hacedor(self):
        for x in self.conjunto:
            if x < self.valMin:
                self.c1.append(x)
            elif x < self.valMax:
                self.c2.append(x)
            elif x > self.valMax:
                self.c3.append(x)
            else :
                self.c4.append(x)
        
        return self.c1, self.c2, self.c3, self.c4   