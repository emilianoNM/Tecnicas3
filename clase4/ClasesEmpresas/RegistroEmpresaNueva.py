# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:03:44 2018

@author: yocoy
"""

class RegistoEmpresaNueva():
    
    def __init__(self, nombre, fechaDeFundacion, objetivos, ubicacion, empresasRelacionadas, sector, inversiones, productos, reemplazo, crecimiento):
        
        self.nombre = nombre
        self.fechaFundacion = fechaDeFundacion
        self.objetivos = objetivos
        self.ubicacion = ubicacion
        self.empresasRelacionadas = empresasRelacionadas
        self.sector = sector
        self.inversiones = inversiones
        self.productos = productos
        self.reemplazo = reemplazo
        self.crecimiento = crecimiento 