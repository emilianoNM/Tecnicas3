# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:06:05 2018

@author: yocoy
"""

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if ord(unaLista[i][0])>ord(unaLista[i+1][0]) or ord(unaLista[i][0])==ord(unaLista[i+1][0]):
                if ord(unaLista[i][0])==ord(unaLista[i+1][0]):
                    for x in range(len(unaLista)):
                        if ord(unaLista[i][x])==ord(unaLista[i+1][x]):
                            temp = unaLista[i]
                            unaLista[i] = unaLista[i+1]
                            unaLista[i+1] = temp
                            break
                    continue
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

unaLista = ["MC Dsi","MC Donalds", "Ford", "Crysler", "Dodge", "Burger King", "Apple"]
ordenamientoBurbuja(unaLista)
print(unaLista)