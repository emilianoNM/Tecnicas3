# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:59:30 2018

@author: yocoy
"""

def factorial(numero):
    fact = 1
    for x in list(range(1, numero)):
        fact *= x
    return fact

def main():
    for x in range(5):
        print(str(x-1)+"! = "+str(factorial(x)))
        
main()