
# coding: utf-8

# In[1]:


#Programa que indica si un numero es par o impar
#Por CBLUELENNON(RVT)


# In[2]:


x=int(input("Ingresa el numero a clasificar\n"))
if(x%2==0 and x!=0):
    print("El numero es PAR")
if(x==0):
    print("El numero que ingresaste es cero")
if(x%2!=0):
    print("El numero es Impar")

