# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:20:17 2018

@author: yocoy
"""

def leerFrase():
    return input("Introduce la frase que deseas invertir: ")

def inversorFrase(frase):
    fraseInvertida = []
    for x in range(len(frase)):
        fraseInvertida.append(frase[len(frase)-1-x])
    return fraseInvertida

def main():
    
    frase = leerFrase()
    print(frase)
    fraseInvertida = inversorFrase(frase)
    nuevaFrase = ""
    for x in fraseInvertida:
        nuevaFrase += str(x)
    print(nuevaFrase)

main()