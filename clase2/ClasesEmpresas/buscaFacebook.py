# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:43:33 2018

@author: Yocoyani Ehecatzin Pérez Ayala
"""

from buscaPagina import buscaPagina as bP
import unicodedata

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def prueba(x,url,cadena):
    
   newurl = ""
    
   for y in range(x,x+len(cadena)):
       newurl += url[y]
       
   print (cadena)
   print(newurl)
   return newurl
    
class buscaFacebook(bP):
    
    def __init__(self, url, usuario):
        bP.__init__(self,url)
        self.usuario = usuario        
    
    def comprobarFacebook(self):
        
        for x in range(len(self.url)):
            comp = prueba(x, self.url,"facebook")
            if comp == "facebook":
               for y in range(len(self.url)):
                   usrTemp = elimina_tildes(self.usuario.lower().split(' ')[0])
                   comp = prueba(y,self.url.lower(),usrTemp)
                   if comp == usrTemp:
                       return True
        return False