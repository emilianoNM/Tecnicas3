# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:42:19 2018

@author: yocoy
"""

import funciones as f

if __name__ == '__main__':
    
    coeficientes = []
    print("Se resolveran ecuaciones de la forma Ax^2+Bx+C")
    print("Introduce A: ", end='')
    coeficientes.append(f.lectura())

    print("Introduce B: ", end='')
    coeficientes.append(f.lectura())
  
    print("Introduce C: ", end='')
    coeficientes.append(f.lectura())
    print("La solucion es: ", f.raices(coeficientes))