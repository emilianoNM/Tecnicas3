# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:13:52 2018

@author: yocoy
"""

import numpy as np

def promedioYSuma(lista):
    
    suma = 0
    for x in lista:
        suma += x
    promedio = suma/len(lista)
    return suma, promedio

def main():
    
    lista = np.random.randint(25, size=100)
    print(lista)
    print(promedioYSuma(lista))

main()