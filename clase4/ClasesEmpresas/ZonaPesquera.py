# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:02:58 2018

@author: yocoy
"""

class ZonaPesquera():
    
    def __init__(self, ubicacion, permisosRequeridos, empresasPrimarias, empresasSecundarias, exportacionProducto, numeroDeBarcos, numeroDeNavegantes, lineasDeTransporte, asociacionesPesqueras, tiposDePez):
        
        self.ubicacion = ubicacion
        self.permisosRequeridos = permisosRequeridos
        self.empresasPrimarias = empresasPrimarias
        self.empresasSecundarias = empresasSecundarias
        self.exportacionProducto = exportacionProducto
        self.numeroDeBarcos = numeroDeBarcos
        self.numeroDeNavegantes = numeroDeNavegantes
        self.lineasDeTransporte = lineasDeTransporte
        self.asociacionesPesqueras = asociacionesPesqueras
        self.tipoDePez = tiposDePez