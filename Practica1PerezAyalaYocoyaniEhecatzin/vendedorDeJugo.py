# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:31:14 2018

@author: yocoy
"""

class vendedorDeJugo:
    
    nombre = "vendedor"
    precio = 0.0
    abierto = False
    
    def __init__(self, nombre, precio, cantidad, jugos):
        
        self.nombre = nombre
        self.precio = precio
        self.abierto = True
        self.cantidad = cantidad
        self.jugos = jugos
     
    def venderJugo(self):    
        print("Vendí un jugo")
        self.cantidad -= 1
    
    def hacerJugo(self):
        print("Has hecho un jugo")
        self.cantidad += 1
    
    def abrir(self):
        if self.abierto != True:
            print("He abierto")
            self.abierto = True
        else:
            print("Ya estaba abierto")
            
    def cerrar(self):
        if self.abierto != False:
            print("He cerrado")
            self.abierto = False
        else:
            print("Ya estaba cerrado")    
        
    def sett(self):
        print(self.nombre,' ',self.precio,' ',self.abierto,' ',self.cantidad,' ', self.jugos)
        
    def cambiarJugo(self, jugo):
        self.jugos = jugo    
    