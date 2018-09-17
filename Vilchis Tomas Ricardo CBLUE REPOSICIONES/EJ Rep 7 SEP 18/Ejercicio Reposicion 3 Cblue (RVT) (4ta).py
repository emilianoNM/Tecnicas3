
# coding: utf-8

# In[1]:


#Programa que eleva un numero ingresado por el usuario a una potencia ingresada tambien por el usuario
#Programa creado por CBLUELENNON (RVT)


# In[2]:


x=int(input("Ingrese el numero que se elevaa a cierta potencia\n"))
y=int(input("Ingrese esa cierta potencia\n"))
elevacion=pow(x,y)
lamismaelevacion=(x**y)
print("El resultado es",elevacion)
print(lamismaelevacion)

