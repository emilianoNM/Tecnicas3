# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:19:34 2018

@author: yocoy
"""

def main():
    
    numeros = [1 for x in range(1, 1000)]
    
    for x in range(2,len(numeros)):
        if numeros[x] == 1:
            for y in range(2, len(numeros)):
                if  y%x == 0 and x != y:
                    numeros[y] = 0
    for x in range(len(numeros)):
        if numeros[x] == 1:
            print(str(x)+' ', end='')
main()