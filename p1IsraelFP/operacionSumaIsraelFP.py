#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:23:11 2018

@author: israel
"""

print "\n\t\t..:Suma Hasta 1800:..\n>> 2 5 7 10 12 15 17 ... 1800"
i=1
b=3
c=3
while i<=1800:
    if(c == 3):
        b = b + c
        c = c - 1
        i += 1
    else:
        b = b + c
        c = c + 1
        i += 1
print "El valor de la suma sucesiva es: ",b