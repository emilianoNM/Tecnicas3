#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:32:25 2018

@author: israel
"""

class Libros:
    def __init__(self,titulo,fechaPublicacion,autor,costo,editorial,paisDeOrigen,noDeCapitulos,noDePaginas,ISBN13,genero):
        self.titulo=titulo
        self.fechaPublicacion=fechaPublicacion
        self.autor=autor
        self.costo=costo
        self.editorial=editorial
        self.paisDeOrigen=paisDeOrigen
        self.noDeCapitulos=noDeCapitulos
        self.noDePaginas=noDePaginas
        self.ISBN13=ISBN13
        self.genero=genero