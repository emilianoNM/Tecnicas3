#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:08:19 2018

@author: israel
"""
print "\n\t\t..:Regresion lineal:..\n> Para una funcion: Y = A + BX"
#Tabla de la reacta:
X = [1,1.8,2,2.5,3,5,15.3]
Y = [1,1.5,2.5,2.8,4,6,17.8]
XY = []
SXY = 0.0
SX = 0.0
SY = 0.0
X2 = []  
SX2 = 0.0
for i in range(len(X)): XY.append(X[i]*Y[i])
for i in range(len(X)): SXY = SXY + XY[i]
for i in range(len(X)): X2.append(pow(X[i],2))
for i in range(len(X)): SX2 = SX2 + X2[i]
for i in range(len(X)): SX = SX + X[i]
for i in range(len(X)): SY = SY + Y[i]

m = ( (len(X)*SXY) - (SX*SY) )/ ( (len(X)*SX2) - (pow(SX,2) ) )
b = (SY - m * SX) / len(X)

print "La funcion es : Y = {} + {} * X".format(b,m)


