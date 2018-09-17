#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:04:05 2018

@author: israel
"""
def fib(f):
    if f == 1: return 1
    if f == 2: return 1
    return fib(f-1)+fib(f-2)
print "\t..:Fibonacci:.."
f=input("Cantidad de no. a hacer en Fibonacci: ")
print "> No. Fibonacci: ",fib(f)
