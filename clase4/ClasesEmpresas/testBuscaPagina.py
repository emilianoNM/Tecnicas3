# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:30:55 2018


@author: Yocoyani Ehecatzin Pérez Ayala
"""

from buscaPagina import buscaPagina as bP

    
url = "https://github.com"
   
pagina = bP(url)
print(pagina.busacadorDePagina())

pagina.setURL("http://www.facebook.com")

print(pagina.busacadorDePagina())