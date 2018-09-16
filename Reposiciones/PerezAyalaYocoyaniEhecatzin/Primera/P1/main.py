# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:59:49 2018

@author: yocoy
"""

import Contador7 as ct

if __name__ == '__main__':
    
    f = ct.Contador7()
    while True:
        f.lector()
        print("Numero de 7: ",f.encuentra())
        desc = input("Si deseas continuar, presiona 1, presiona cualquier otra en caso contrario: ")
        if desc == '1':
            break
        