#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:22:57 2018

@author: israel
"""
import functools, operator
print "\t..:Factorial:.."
d = input(">Dame el numero a factorizar: ")
if(d>0): print "El factorial es: ",functools.reduce(operator.mul,xrange(1,d))
else: print "Error ... El numero debe ser mayor a 0"