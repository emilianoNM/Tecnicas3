# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:59:12 2018

@author: yocoy
"""

import vendedorDeJugo as vj

if __name__ == '__main__':
    
    v1 = vj.vendedorDeJugo("Jhon", 20.50, 100, "Limon")
    v1.abrir()
    v1.cerrar()
    v1.sett()
    v1.hacerJugo()
    v1.venderJugo()
    v1.cambiarJugo("Manzana")
    v1.sett()