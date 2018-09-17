#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:34:01 2018

@author: israel
"""

def matrizDefinida():
    return [[0,0],[0,0]]

def menu():
    matriz = matrizDefinida()
    print("\t...:Matriz Definida:...\n\tSe tiene una matriz 2x2")
    print("\t\t[a,b]\n\t\t[c,d]")
    
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            valor = 0
            print "Dame el valor a asignar [",i,"]","[",j,"]:"
            valor = int(input(">> "))
            matriz[i][j] = valor
    return matriz

def matrizTranspuesta(A):
    B = [[0,0],[0,0]]
    print("\nLa transpuesta de la matriz es:\n")
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    for array in B: print(array)
    
def matrizDeterminante(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    print "\nLa determinante de la matriz es: ",det
    
def matrizTraza(A):
    trz = A[0][0] + A[1][1]
    print "\nLa traza de la matriz es: ", trz

def imprimir(A):
    print("\n**Matriz Asignada**")
    for array in A: print(array)
 
matrizDef = menu()       
while True:
    imprimir(matrizDef)
    print("\nMenu:\n1)Matriz Transpuesta\n2)Traza\n3)Determinante\n4)Salir")
    opcMenu=int(input("Selecciona una opcion: "))
    if(opcMenu==1): matrizTranspuesta(matrizDef)
    elif(opcMenu==2): matrizTraza(matrizDef)
    elif(opcMenu==3): matrizDeterminante(matrizDef)
    elif(opcMenu==4):
        print("Fin del programa ...")
        break
    else:
        print("ELije uno de los valores del menu")
        

