#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:33:41 2018

@author: israel
"""
size = input("\t\t..:Cuadrado:..\n>Dame la dimension del cuadrado nxn: ")
inner_size = size - 2
print("*" * size)
for i in range(inner_size): print("*"+ " "*inner_size + "*")
print("*" * size)