#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:24:35 2018

@author: israel
"""

#MergeSort to TECNICAS 3
def bubbleSort(A):
    for i in range(1,len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                tmp=A[j]
                A[j]=A[j+1]
                A[j+1]=tmp
    return A
list=["Juan","Carlos","Estefania","Alejandro","Cesia"]
print "Lista original: ",list
print "Lista ordenada: \n",bubbleSort(list)