# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:41:15 2018

@author: yocoy
"""

class CuentaAdmin():
    
    def __init__(self, nombre, clave, contraseñaPrimerNivel, identificadorDeSeccion, puesto, codigoDeNivel, rachaDeContribucion, modificacionesRecientes, ultimaSesion, usuarioNormal):
        
        self.nombre = nombre
        self.clave = clave
        self.contraseñaPrimerNivel = contraseñaPrimerNivel
        self.identificadorSeccion = identificadorDeSeccion
        self.puesto = puesto
        self.codigoDeNivel = codigoDeNivel
        self.rachaDeContribucion = rachaDeContribucion
        self.modificacionesRecientes = modificacionesRecientes
        self.ultimaSesion = ultimaSesion
        self.usuarioNormal = usuarioNormal
        
        