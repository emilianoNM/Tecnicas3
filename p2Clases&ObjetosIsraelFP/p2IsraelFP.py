#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:53:28 2018

@author: israel
"""
import os
class escuela:
    def _init_(self,raiz):
        self.raiz=raiz
class cuenta:
    def _init_(self,nombre,edad,noCuenta,materia,correo,carrera):
        self.nombre = nombre
        self.edad = edad
        self.noCuenta = noCuenta
        self.correo = correo
        self.carrera = carrera
        
    def obtenerNombre(self):
        nombre = raw_input("> Escribe tu nombre completo: ")
        self.nombre=nombre
        
    def edad(self):
        edad = int(input("> Dame tu edad: "))
        self.edad=edad
    
    def noCuenta(self):
        numeroCuenta = int(input("> Escribe tu No. de cuenta (8 digitos): "))
        self.noCuenta = numeroCuenta
    
    def materia(self):
        materia = raw_input("> Escribe la materia a inscribir: ")
        self.materia = materia
    
    def correo(self):
        correo = raw_input("> Escribe tu correo de contacto: ")
        self.correo = correo
        
    def carrera(self):
        while True:
            print "> Carrera\n\t1)Computacion\n\t2)Electrica\n\t3)Mecanica\n\t4)Industrial\n\t5)Mecatronica"
            opc = int(input("> Selecciona la carrera que perteneces: "))
            if(opc == 1): 
                self.carrera = "Computacion"
                break
            elif(opc == 2):
                self.carrera = "Electrica"
                break
            elif(opc == 3):
                self.carrera = "Mecanica"
                break
            elif(opc == 4):
                self.carrera = "Industrial"
                break
            elif(opc == 5):
                self.carrera = "Mecatronica"
                break
            else: print "Error, selecciona una de las opciones"

cuenta1=cuenta()
escuela.raiz=cuenta1

while True:
    os.system('clear')
    print "\n\t\t==========<Sistema de Inscripcion>=========="
    cuenta1 = cuenta()
    for i in range(1,7):
        if(i==1): cuenta1.obtenerNombre()
        elif(i==2): cuenta1.edad()
        elif(i==3): cuenta1.noCuenta()
        elif(i==4): cuenta1.materia()
        elif(i==5): cuenta1.correo()
        elif(i==6): cuenta1.carrera()
    
    print "\n> Nombre: {}\n>Edad: {}\n>No. Cuenta: {}\n>Materia: {}\n>Correo: {}\n>Carrera: {}".format(cuenta1.nombre,cuenta1.edad,cuenta1.noCuenta,cuenta1.materia,cuenta1.correo,cuenta1.carrera)
    break