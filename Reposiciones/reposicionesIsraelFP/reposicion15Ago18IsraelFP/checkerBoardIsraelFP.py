#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:38:32 2018

@author: israel
"""
import numpy as np

print "\t\t..:CheckerBoard pattern:.."
def printCheckerBoard(n):
    x = np.zeros((n,n),dtype = str)
    x[1::2,::2] = "*"
    x[::2,1::2] = " "
    
    for i in range(n):
        for j in range(n):
            print(x[i][j]," ")
        else: print()
printCheckerBoard(8)