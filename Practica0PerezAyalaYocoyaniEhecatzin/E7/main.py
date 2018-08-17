# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:58:29 2018

@author: yocoy
"""

def main():
    while True:
        try :
            tiempo = float(input("Introduce el tiempo a calcular: "))
            break
        except :
            print("VALOR INVALIDO")
    if tiempo != 0:
        volumen = float(180/(30+2*tiempo))
        rC = float((volumen-180)/tiempo)
        print("La razon de cambio en el tiempo ",tiempo,"s es ",rC,"cm^3/s")

main()