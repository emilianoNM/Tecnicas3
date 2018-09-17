#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:45:00 2018

@author: israel
Ley de Boyle en P(t) = 30 + 2t
"""
while True:
    print "\n\t\t..:Ley de Boyle:..\n> Dado a P * V = K en funcion de:\n\t\t P(t)= 30 + 2t"
    print ">>  Resuelto:  dV = - 2*k /(30 + 2*t) donde k = 1800 cm Hg * cm³"
    t = float(input("\rDame el valor t (segundos): "))
    if(t < 0):
        print "Error ... No hay tiempos negativos"
        break
    dV =- (3600.0)/(pow((30 + 2*t),2))
    print dV
    print "\t\tdV = {} cm³/s \nNota: el valor negativo indica disminucion".format(dV)
    break