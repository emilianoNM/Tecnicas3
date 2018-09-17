#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:49:51 2018

@author: israel
"""

class StackEmpresa:
    def __init__(self):
        self.__items = []
    def isEmpty(self):
        return self.__items == []
    def push(self,item):
        self.__items.insert(0,item)
    def pop(self):
        return self.__items.pop(0)
    def size(self):
        return len(self.__items)
    def __str__(self):
        return "Stack: {}".format(self.__items)

s = StackEmpresa()
s.push("Hello World")
s.push("True")
print (s.pop())
s.push(4)
print(s.isEmpty())
print(s.size())
print(s)
