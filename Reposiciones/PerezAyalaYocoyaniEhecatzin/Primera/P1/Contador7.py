# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:54:01 2018

@author: yocoy
"""

class Contador7():
    
    def __init__(self):
       self.numero = ""
    
    def lector(self):
    
        while True:
            try:
                self.numero = str(int(input("Introduce el numero: ")))
                break
            except:
                print("Numero invalido, intenta otra vez")
        
    def encuentra(self):
        
        contador = 0
        for x in self.numero:
            if x == '7':
                contador +=1
        return contador