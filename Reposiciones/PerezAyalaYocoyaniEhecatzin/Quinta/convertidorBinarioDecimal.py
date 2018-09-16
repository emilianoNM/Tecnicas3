# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:36:21 2018

@author: yocoy
"""

def lectura():
    while True:
        try:
            numero = input("Introduce el numero: ")
            for x in numero:
                if x != '0' and x != '1':
                    0/0
            break
        except:
            print("Numero no valido")
    return numero

def convertidorBinarioDecimal(numero):
    nuevoNumero = 0
    for x in range(len(numero)):
        nuevoNumero += (2**(x))*(int(numero[len(numero)-1-x]))
    return nuevoNumero

def main():
    numeroBinario = lectura()
    print(convertidorBinarioDecimal(numeroBinario))
main()
    