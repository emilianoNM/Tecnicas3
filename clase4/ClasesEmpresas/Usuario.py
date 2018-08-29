# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:47:25 2018

@author: yocoy
"""

class usuario():
    
    def __init__(self, nombreDeUsuario, iD, password, correo, intereses, ocupacion, descripcion, nivelDeUsuario, telefono, tarjetaDeCredito):
        
        self.nombreDeUsuario = nombreDeUsuario
        self.__iD = iD
        self.__password = password
        self.__correo = correo
        self.intereses = intereses
        self.ocupacion = ocupacion
        self.descripcion = descripcion
        self.nivelDeUsuario = nivelDeUsuario
        self.__telefono = telefono
        self.__tarjetaDeCredito = tarjetaDeCredito