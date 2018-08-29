# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:57:50 2018

@author: yocoy
"""

class Mapa():
    
    def __init__(self, ubicacionDeReferencia, ubicacionesMultiples, mapaEmpresarial, mapaRelacionesEmpresariales, mapaTransporteMaterias, mapaEnviosProductos, empresasDeLaZona, regionDeComercio, sucursales):
        
        self.ubicacionDeReferencia = ubicacionDeReferencia
        self.ubicacionesMultiples = ubicacionesMultiples
        self.mapaEmpresarial = mapaEmpresarial
        self.mapaRelacionesEmpresariales = mapaRelacionesEmpresariales
        self.mapaTransporteMaterias = mapaTransporteMaterias
        self.mapaEnviosProductos = mapaEnviosProductos
        self.empresasDeLaZona = empresasDeLaZona
        self.regionDeComercio = regionDeComercio
        self.sucursales = sucursales