# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:17:08 2018

@author: Yocoyani Ehecatzin Pérez Ayala

"""
import requests
import sys

class buscaPagina(object):
    
    def __init__(self, url):
        self.url = url
    
    def busacadorDePagina(self):
        while True:
            try:
                r = requests.get(self.url)
                break
            except:
                return False
        if r.status_code != 200:
            sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, self.url))
            return None

        return True
    
    def setURL(self, url):
        self.url = url
        