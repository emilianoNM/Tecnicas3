# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:20:05 2018

@author: yocoy
"""

class Empresa():
    
    _pila = []
        
    @classmethod
    def pilaPoblacionAgregar(cls, nombre):
        cls._pila.append(nombre)
        
    @classmethod 
    def desplegarPila(cls):
        return cls._pila
    
    @classmethod
    def quitarElemento(cls):
        return cls._pila.pop()
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.pilaPoblacionAgregar(self.nombre)
        
def main():
    
    hamburgueseria = Empresa("MC Donald's")
    carros = Empresa("Ford")
    print(hamburgueseria)
    print(carros)
    print (carros.desplegarPila())
    print(hamburgueseria.desplegarPila())
    print(hamburgueseria.quitarElemento())
    print(hamburgueseria.desplegarPila())
    
main()