# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:16:03 2018

@author: yocoy
"""


def main():
    
    datos = [[1,1],[1.8,1.5],[2,2.5],[2.5,2.8],[3,4],[5,6],[15.3,17.8]]
    sumaX=0
    sumaY=0
    sumaXY=0
    sumaXC=0
    
    for x in datos: 
        sumaX += x[0]
    print(sumaX)
    for y in datos:
        sumaY += y[1]
    print(sumaY)
    for xy in datos:
        sumaXY += xy[0]*xy[1]
    print(sumaXY)
    for xc in datos:
        sumaXC += xc[0]**2
    print(sumaXC)
    n=len(datos)
    
    a= (n*sumaXY-sumaX*sumaY)/(n*sumaXC-(sumaX**2))
    b = (sumaY-a*sumaX)/n
    
    print(b,"+",a,"x")
    
main()