# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:18:59 2018

@author: Yocoyani Ehecatzin Perez Ayala
"""

class Buscador():
    
    def __init__(self, nombreDeLaEmpresa, estado, categoria, sectorDeInteres, buscadorInternet, producto, sucursal, precisionBusqueda,tiempoBusqueda,subEmpresas,departamento):
        
        self.nombreDeLaEmpresa = nombreDeLaEmpresa
        self.estado = estado
        self.categoria = categoria
        self.sectorDeInteres = sectorDeInteres
        self.buscadorInternet = buscadorInternet
        self.sucursal = sucursal
        self.presicionBusqueda = precisionBusqueda
        self.tiempoBusqueda = tiempoBusqueda
        self.subEmpresas = subEmpresas
        self.departamento = departamento