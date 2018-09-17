#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:04:29 2018

@author: israel
"""
data=[]
def operaciones(data):
    #suma=0
    #for i in range(0,len(data)): suma=suma+data[i]
    print "\nSuma: ",sum(data)
    print "Promedio: ", sum(data) / float(len(data))
    print "Producto: ", reduce((lambda x, y: x*y),data)
    print "Menor valor: ",min(data)
    print "Mayor valor: ",max(data)

for i in range(1,4):
    print("Dame el valor {}: ".format(i))
    tmp = input()
    data.append(tmp)

operaciones(data)
