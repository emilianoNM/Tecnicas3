# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 18:40:11 2018

@author: yocoy
"""
import numpy as np

def distance(p1,p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
def leerNum():
    while True:
        try:
            numero = float(input("Numero: "))
            break
        except:
            print("Formato invalido, trata otra vez")
    return numero

def main():
    p1 = []
    p2 = []
    print("Introduce las coordenadas del primer punto: ")
    p1.append(leerNum())
    p1.append(leerNum())
    print("Introduce las coordenadas del segundo punto: ")
    p2.append(leerNum())
    p2.append(leerNum())
    print("La distancia entre los puntos es: ",distance(p1,p2))
    
main()