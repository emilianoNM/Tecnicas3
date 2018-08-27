#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:40:45 2018

@author: israel
"""
from p2Dulce import Dulce

class Tienda(Dulce):
    def __init__(self,nombreTienda,cantidad,costoFinal,nombre,marca,precio):
        Dulce.__init__(self,nombre,marca,precio)
        self.nombreTienda = nombreTienda
        self.cantidad = cantidad
        self.costoFinal = costoFinal

    @property #Getter
    def nombretienda(self): return self.nombreTienda

    @property #Getter
    def cantidad(self): return self.cantidad

    @property #Getter
    def costoFinal(self): return self.costoFinal

    @nombretienda.setter
    def nombretienda(self,nombreTienda): self.nombreTienda = nombreTienda

    @cantidad.setter
    def cantidad(self,cantidad): self.cantidad = cantidad

    @costoFinal.setter
    def costoFinal(self,costoFinal): self.costoFinal = self.precio + 5

    def __str__(self): return ">TIENDA\n\tNombre Tienda: {}\n\tCantidad: {}\n\tCosto Final:{}\n".format(self.nombreTienda,self.cantidad,self.costoFinal)
