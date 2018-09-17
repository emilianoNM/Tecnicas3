#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:20:48 2018

@author: israel
"""
num = input("\t\t..:Triangulo Inf. Izquierdo:..\n>Dame el no. filas: ")
#Pattern A
for a in range(num):
    for i in range(a):
        print "*",
    print ""