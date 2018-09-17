#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 23:43:58 2018

@author: israel
"""

while True:
    print("..:Puntos de Corte de No. Enteros:..\n\t\tDesde dos puntos: a - b")
    a=int(input(">Dame el valor de 'a' (inferior): "))
    b=int(input(">Dame el valor de 'b' (superior): "))
    if(a==b):
        print("Error ... el valor 'inferior' debe ser diferente de 'superior'")
        break
    data = [a,b]
    i=1
    print(">Dame 10 no. enteros:")
    while i<11:
        print '\n>Dame el valor [',i,']: '
        c=int(input("\r\r>> \r"))
        if(c>=a and c<=b):
            data.append(c)
            i+=1
        else: print "Error ... asigna un valor dentro del rango: ",a,"a",b
    data.sort()
    print "Lista de Numeros Enteros Ordenados:\n", data
    break