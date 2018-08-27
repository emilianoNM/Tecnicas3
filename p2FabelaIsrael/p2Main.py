#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 19:37:11 2018

@author: israel
"""
from p2Tienda import Tienda

def main():
    print "\n\t\t..:Main:.."
    miTienda = Tienda("El guero",5,13,"CarlosV","Nestle",5)
    print miTienda.productoDulce()
    print miTienda


if __name__ == '__main__':
    while True:
        main()
        break
