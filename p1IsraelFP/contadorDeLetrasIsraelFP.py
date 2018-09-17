#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:08:36 2018

@author: israel

Examples:
    print(len(palabra))
    print(letra==palabra[0])
"""
print("\t\t..:Contador de Letras:..")
print("*Nota: Solo se aceptan palabras letras en Mayusculas y minusculas, sin ningun numero*")
palabra = raw_input(">Dame la palabra: ")
letra = raw_input(">Cual letra se va a contar: ")
total = 0

for i in range(len(palabra)):
    if letra == palabra[i]:
        total += 1

print "La letra - ",letra," - se encontro ",total," veces de la palabra: ",palabra
