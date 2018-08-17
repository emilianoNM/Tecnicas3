# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:09:14 2018

@author: yocoy
"""

def main():
    
    limite = 15
    suma = 0
    for x in range(limite+1):
        suma += (1/(x+1))
    print("El resultado es: ",suma)

main()