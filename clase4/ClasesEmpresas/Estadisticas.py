# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:58:01 2018

@author: yocoy
"""

class Estadisticas():
    
    def __init__(self, tipo, sector, zona, opcionDeComparacion, graficos, informacionDatos, archivos, comparacion, fuente, tamañoMuestra):
        
        self.tipo = tipo
        self.sector = sector
        self.zona = zona
        self.opcionDeComparacion = opcionDeComparacion
        self.graficos = graficos
        self.informacionDatos = informacionDatos
        self.archivos = archivos
        self.comparacion = comparacion
        self.fuente = fuente
        self.tamañoDeMuestra = tamañoMuestra