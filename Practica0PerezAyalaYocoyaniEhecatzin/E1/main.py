# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:54:00 2018

@author: yocoy
"""
import KelvinToFahrenheit as KTF 

if __name__=='__main__':
    while True:
        while True:
            try:
                kelvin = float(input("Introduce el valor en Kelvin a convertir: "))
                break
            except :
                print("Los datos de entrada son invalidos\n vuelve a intentar")
        far = KTF.convertidorKF(kelvin)
        print("El valor es: ")
        print(far.conv())
        while True:
            try:
                decision = int (input("Si deseas salir presiona 1, en caso contrario presiona cualquier otro numero: "))
                break
            except :
                print("Entrada no valida, intenta otra vez")
                
        if decision == 1:
            break
        