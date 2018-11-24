#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = input('Ingrese a: ')
b = input('Ingrese b: ')
c = input('Ingrese c: ')
 
discriminante = b ** 2 - 4 * a * c
if discriminante < 0:
    print 'La ecuacion no tiene soluciones reales'
elif discriminante == 0:
    x = -b / (2 * a)
    print 'La solucion unica es x =', x
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    print 'Las dos soluciones reales son:'
    print 'x1 =', x1
    print 'x2 =', x2
input()

