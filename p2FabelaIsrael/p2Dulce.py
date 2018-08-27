#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:59:12 2018

@author: israel
"""

class Dulce:
    def __init__(self,nombre,marca,precio):
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        
    #def __str__(self): return ">PRODUCTO\n\tNombre: {}\n\tMarca: {}\n\tPrecio:{}".format(self.nombre,self.marca,self.precio)
    def productoDulce(self): return ">PRODUCTO\n\tNombre: {}\n\tMarca: {}\n\tPrecio:{}".format(self.nombre,self.marca,self.precio)
    
    @property
    def nombre(self): return self.nombre
    
    @property
    def marca(self): return self.marca
    
    @property
    def precio(self): return self.precio
    
    @nombre.setter
    def nombre(self,nombre): self.nombre=nombre
    
    @marca.setter
    def marca(self,marca): self.marca=marca
    
    @precio.setter
    def precio(self,precio): self.precio=precio