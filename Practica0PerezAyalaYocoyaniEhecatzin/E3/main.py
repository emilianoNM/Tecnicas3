# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:44:58 2018

@author: yocoy
"""
import numpy as np
import Matematico as mt

matematico = mt.Matematico(np.zeros((2,2)))

if __name__=='__main__':
    
    while True:
        while True:
            try:        
                print("Seleciona que quieres hacer\n1)Capturar matriz\n2)Obtener transpuesta\n3)Obtener traza\n4)Salir del programa")
                seleccion = int(input("--> "))
                break
            except :
                print("Entrada no valida")
            
        if  seleccion == 1:
            matematico.get(mt.capturaMatriz())
        elif seleccion == 2:
            print("La transpuesta es: ")
            for x in matematico.matrizTranspuesta():
                print(x)
        elif seleccion==3:
            print("La traza es: ",matematico.traza())
        elif seleccion==4:
            break
        else :
            print("SELECCION NO VALIDA")