# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:12:14 2018

@author: yocoy
"""

class Contador:
    
    def __init__(self, caracter, cadena):
        self.caracter = caracter
        self.cadena = cadena
        
    def cuenta(self):
        cuenta = 0
        for x in self.cadena:
            if self.caracter[0] == x:
                cuenta += 1
        return cuenta
        