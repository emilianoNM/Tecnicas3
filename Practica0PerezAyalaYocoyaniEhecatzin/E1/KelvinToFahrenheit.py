# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:41:06 2018

@author: yocoy
"""

class convertidorKF:
    
    def __init__(self,kelvin):
        self.kelvin = float(kelvin)
    
    def conv(self):
        return 1.8 * (self.kelvin - 273.15) + 32
