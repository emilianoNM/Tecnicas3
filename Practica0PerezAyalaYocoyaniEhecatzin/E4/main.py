# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:05:12 2018

@author: yocoy
"""

import Conjuntos as cj

if __name__ == '__main__':
    
    while True:
        conjunto = []
        while True:
            try:
                val1 = int(input("Introduce el primer valor de corte: "))
                break
            except :
                print("Valor invalido")
        while True:
            try:
                val2 = int(input("Introduce el segundo valor de corte: "))
                break
            except :
                print("Valor invalido")
        
        while True:
            while True:
                try:
                    conjunto.append(int(input("Introduce el elemento del conjunto: ")))
                    break
                except :
                    print("VALOR INGRESADO INVALIDO")
            while True:
                try :
                    decision = int(input("Si son todos los elementos, presiona 1, en caso contrario presiona cualquier numero: "))
                    break
                except :
                    print("Decision no valida")
            if decision == 1:
                break
            
        if val1 < val2:
            cortador = cj.Conjuntos(conjunto, val1, val2)
        elif val2>val1:
            cortador = cj.Conjuntos(conjunto, val2, val1)
        else :
            print("Los valores de corte no pueden ser iguales, intenta otra vez")
            continue
        
        print(cortador.hacedor())
        
        while True:
            try :
                decision = int(input("Si deseas terminar, presiona 1, en caso contrario presiona cualquier numero: "))
                break
            except :
                print("Decision no valida")
        if decision == 1:
            break