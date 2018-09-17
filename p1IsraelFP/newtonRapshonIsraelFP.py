#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:49:14 2018

@author: israel
"""
print "\n\t\t...:Newton-Raphson:...\n>> f(X) = e**-x + ln x"

import math as mt

def f(x): return  mt.exp(-x)+mt.log(x)
def Df(x): return -mt.exp(-x)+(1/x)

x0 = 1.0
error = 10
i = 1
while error > 1e-6:
    x1 = x0 - f(x0)/Df(x0)
    error = abs(x1-x0 )
    x0=x1
    i+=1
    print "La iteracion {} , es de aproximacion: {}".format(i,x0)
