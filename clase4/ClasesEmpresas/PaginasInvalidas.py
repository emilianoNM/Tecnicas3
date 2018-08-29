# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:25:29 2018

@author: yocoy
"""

class PaginasInvalidas():
    
    def __inti__(self, empresa, url, pagRealVerif, pagInvalidVerif, ultimaVerificacion, ultimaModific, vecesValid, vecesInvalid, puntuacionEmpr, pagSinRelacion):
        
        self.empresa = empresa
        self.url = url
        self.pagRealVerif = pagRealVerif
        self.pagInvalidVerif = pagInvalidVerif
        self.ultimaVerificacion = ultimaVerificacion
        self.ultimaModificacion = ultimaModific
        self.vecesInvalid = vecesInvalid
        self.vecesValid = vecesValid
        self.puntuacionEmpr = puntuacionEmpr
        self.pagSinRelacion = pagSinRelacion