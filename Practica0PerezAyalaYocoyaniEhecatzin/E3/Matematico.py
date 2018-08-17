# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:38:51 2018

@author: yocoy
"""
import numpy as np

def capturaMatriz():
    
    matriz = np.zeros((2,2))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            while True:
                try:        
                    print("Introduce el numero ", i ,"x", j ,": ", end="")
                    matriz[i][j] = float(input())
                    break
                except :
                    print("ENTRADA INVALIDA")
    return matriz

class Matematico:
    
    def __init__(self, matriz):
        self.matriz = matriz
        
    def get(self, matriz):
        self.matriz = matriz 
    
    def matrizTranspuesta(self):
        matrizTranspuesta = np.zeros((2,2), dtype=float)
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                matrizTranspuesta[y][x] = self.matriz[x][y]
        return matrizTranspuesta
                
    def traza(self):
        traza = []
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                if x==y:
                    traza.append(self.matriz[x][y])
        return traza