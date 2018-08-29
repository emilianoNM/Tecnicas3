
# coding: utf-8

# In[ ]:



ancho = int(input("Ancho: "))

for x in range(1, ancho+1):
	print " "*(ancho - (x/2))+"*"*x
for y in range (ancho-1, 0, -1):
	print " "*(ancho - (y/2))+"*"*y

