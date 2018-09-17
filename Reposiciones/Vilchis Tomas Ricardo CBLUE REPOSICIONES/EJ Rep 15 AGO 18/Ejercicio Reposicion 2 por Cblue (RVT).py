
# coding: utf-8

# In[1]:


#Programa que obtiene el area de un circulo de acuerdo al radio  proporcionado por el usuario
#Por CBLUELENNON (RVT)


# In[2]:


import math
radio=int(input("Ingrese el radio de la circunferencia de la cual desea calcular su area\n"))


# In[3]:


radioalcuadrado=(radio**2)
area=( math.pi *radioalcuadrado)
print("El area de la circunferencia es:",area, "Unidades cuadradas o de area :)")

