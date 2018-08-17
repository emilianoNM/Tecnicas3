# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:18:30 2018

@author: yocoy
"""

import Contador as ct

if __name__ == '__main__':
    while True:
        
        while True:
            try:
                caracter = str(input("Introduce el caracter a contar: "))
                if len(caracter) <= 1 and len(caracter) > 0:
                   break
            except :
                print("Entrada no valida, se necesita un caracter como dato")
        
        while True:
            try:
                cadena = str(input("Introduce la cadena a revisar: "))
                break
            except :
                print("Entrada no valida, se necesita un caracter como dato")
        
        contador = ct.Contador(caracter,cadena)
        print("El numero de veces que se repite el caracter son: ", end='')
        print(contador.cuenta())
        while True:
            try:
                decision = int (input("Si deseas salir presiona 1, en caso contrario presiona cualquier otro numero: "))
                break
            except :
                print("Entrada no valida, intenta otra vez")
                
        if decision == 1:
            break
        