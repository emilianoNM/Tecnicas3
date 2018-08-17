# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:40:57 2018

@author: yocoy
"""
import numpy as np

def fun(x):
	
    x = np.exp(-x) + np.log(x)
    return x

def dfun(x):
	
    x = -np.exp(-x)+(1/x)
    return x
 
def main ():
	
    tol = 0.00001
    xi = 1.0
    
    x = xi-fun(xi)/dfun(xi)
    
    error = abs((x-xi)/x)
    
    while error > tol:
        xant = x
        x = x-fun(x)/dfun(x)
        error = abs((x-xant)/x)
    print (x)
    
main()