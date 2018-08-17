# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:50:02 2018

@author: yocoy
"""

def main():
    
    termino = 0
    suma = 0
    contador = 0
    
    while termino <= 1800:
        print(termino)
        suma += termino
        if contador%2 == 0:
            termino += 2
        else:
            termino +=3
        contador += 1
    print("Suma: ", suma)
main()