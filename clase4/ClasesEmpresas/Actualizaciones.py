# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:39:11 2018

@author: yocoy
"""

class Actualizaciones():
    
    def __init__(self, baseDD, archivos, fecha, persona, verifacion, tamaño, clave, iDAdmin, contraseñaGlobal, tiempoDeActualizacion):
        
        self.baseDD = baseDD
        self.archivos = archivos
        self.fecha = fecha
        self.persona = persona
        self.verificacion = verifacion
        self.tamaño = tamaño
        self.__clave = clave
        self.__iDAdmin = iDAdmin
        self.__contraseñaGlobal = contraseñaGlobal
        self.timpoDeActualizacion = tiempoDeActualizacion