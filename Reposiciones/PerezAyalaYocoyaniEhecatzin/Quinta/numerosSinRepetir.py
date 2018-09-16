# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:43:16 2018

@author: yocoy
"""

def lectura():
    while True:
        try:
            v = int(input("Valor entre 10 y 100: "))
            if v <= 100 and v >= 10:
                break
            print("Valor invalido")
            continue
        except :
            print("Valor no valido, intenta de nuevo")
    return v

def main():
    
    numeros = []
    for x in range(25):
        lec = lectura()
        if lec not in numeros:
            numeros.append(lec)
    print (numeros)
main()