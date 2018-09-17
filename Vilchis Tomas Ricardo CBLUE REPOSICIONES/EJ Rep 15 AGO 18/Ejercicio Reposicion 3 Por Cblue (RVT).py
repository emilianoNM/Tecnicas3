
# coding: utf-8

# In[1]:


#Programa que imprime las tablas de multiplicar de cierto numero indicado por el usuario
#Creado por CBLUELENNON (RVT)


# In[2]:


tabla=int(input("Ingresa el numero del cual quieres generar la tabla de multiplicar"))
for i in range (1,11):
    tablamult=((tabla*i))
    print(tabla,"X",i,"=",tablamult)

