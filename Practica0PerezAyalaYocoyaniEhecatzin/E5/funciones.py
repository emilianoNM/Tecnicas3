# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:23:03 2018

@author: yocoy
"""
import numpy as np

def raices(coeficientes):
    
    raiz = []
    discriminante = float((coeficientes[1]**2)-4*coeficientes[0]*coeficientes[2])
    
    if discriminante > 0:
        raiz.append((-coeficientes[1]+np.sqrt(discriminante))/(2*coeficientes[0]))
        raiz.append((-coeficientes[1]-np.sqrt(discriminante))/(2*coeficientes[0]))
        return raiz
    elif discriminante == 0:
        raiz = (-coeficientes[1])/(2*coeficientes[0])
        return raiz
    else :
        raiz.append(str(-coeficientes[1]/(2*coeficientes[0]))+' + '+str(abs(np.sqrt(-discriminante)/2))+' i')
        raiz.append(str(-coeficientes[1]/(2*coeficientes[0]))+' - '+str(abs(np.sqrt(-discriminante)/2))+' i')
        
    return raiz

def lectura():
    while True:
        try :
            vL = float(input())
            break
        except :
            print("Valor invalido")
    return vL