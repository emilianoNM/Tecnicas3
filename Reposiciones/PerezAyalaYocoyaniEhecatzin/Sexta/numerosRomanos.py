# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:23:42 2018

@author: yocoy
"""
import math

Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

def convertidorRomano(N):
    
    u= N % 10
    d=int(math.floor(N/10))%10
    c=int(math.floor(N/100))
    if(N>=100): 
        print(Centena[c]+Decena[d]+Unidad[u], end=' ')
    else:
        if(N>=10):
            print(Decena[d]+Unidad[u], end = ' ')
        else:
            print(Unidad[N], end = ' ')

def main():
    for x in range(0,500):
        convertidorRomano(x)

main()