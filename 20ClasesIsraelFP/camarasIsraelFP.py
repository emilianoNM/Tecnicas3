#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:59:09 2018

@author: israel
"""
class Camaras:
    def __init__(self,fabricante,modelo,tipo,categoria,precio,fechaDeSalida,material,peso,resolucion,longitudFocal,zoom):
        self.fabricante=fabricante
        self.modelo=modelo
        self.tipo=tipo
        self.categoria=categoria
        self.precio=precio
        self.fechaDeSalida=fechaDeSalida
        self.material=material
        self.peso=peso
        self.resolucion=resolucion
        self.longitudFocal=longitudFocal
        self.zoom=zoom