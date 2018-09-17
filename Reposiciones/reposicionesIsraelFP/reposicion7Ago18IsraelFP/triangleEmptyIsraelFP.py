#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 20:08:47 2018

@author: israel
"""

lines = int(input("\t\t..:Empty Triangle:..\n> Dame el no. de lineas para el Triangulo: "))
print (lines-1) * " " + "* "
for i in xrange(1,lines-1): print (lines-1-i) * " " + "*" + (2*i-1) * " " + "* "
print (lines) * "* "