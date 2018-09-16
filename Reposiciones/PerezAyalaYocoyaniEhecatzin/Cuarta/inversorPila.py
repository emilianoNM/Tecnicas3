# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:55:46 2018

@author: yocoy
"""

import numpy as np

def inversorPila(pila):
    y = []
    print("Hey")
    print(len(pila))
    for x in range(len(pila)):
        y.append(pila[len(pila)-1-x])
    return y

def main():
    pilaOriginal = np.random.randint(10, size=10)
    pilaInvertida = inversorPila(pilaOriginal)
    print(pilaOriginal)
    print(pilaInvertida)
    
main()