#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:09:06 2018

@author: israel
"""
import math

while True:
    print "\n\t\t..:Chicharronera:..\n\tFormula General:\tAx²+Bx+C"
    A = int(input("\r>> Dame el valor de 'A': "))
    B = int(input("\r>> Dame el valor de 'B': "))
    C = int(input("\r>> Dame el valor de 'C': "))
    if (A==0):
        print("Error ... 'A' debe ser diferente de 0 (cero)")
        break
    """
    R = -B +- sqrt(B²-4AC)/ (2A)
    """
    R = pow(B,2) - 4 * A * C
    d = 2 * A
    if(R == 0):
        X = -B / d
        print "X = {}".format(X)
    elif(R > 0):
        X1 = ((-B + math.sqrt(R)) / d)
        X2 = ((-B - math.sqrt(R)) / d)
        print "X1 = {} \nX2 = {}".format(X1,X2)
    else:
        r = (-B / d)
        X = (math.sqrt(-R) / d)
        print "X1 = {} + {} i \nX2 = {} - {} i".format(r,X,r,X)
    break