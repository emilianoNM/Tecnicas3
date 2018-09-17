
# coding: utf-8

# In[1]:


#Programa que lea del usuario un numero entero real positivo y calcule su factorial
#Creado por CBLUELENNON


# In[2]:


x=int(input("Dame un numero entero positivo porfavor\n"))

print("El numero que ingresaste es",x)
i=1
y=x
while(x>=1 and i<=x-1):
    fact=y*(x-i)
    y=fact
    i=i+1
print("El factorial de",x,"es:",y)

