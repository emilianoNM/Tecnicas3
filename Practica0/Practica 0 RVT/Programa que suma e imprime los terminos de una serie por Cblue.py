
# coding: utf-8

# In[1]:


print("Programa que obtenga la suma e imprima los términos de la siguiente serie: 2, 5, 7, 10, 12, 15, 17,…, 1800")


# In[2]:


i=2
x=2
lista=[]
while(x>=2 and x<=1800):
    lista.append(x)
    if(i%2==0 or i==0):
        x=x+3
        i=i+1
        
    elif(i%2!=0):
        x=x+2
        i=i+1


# In[3]:


print("Los numeros de la serie son los siguientes")
for y in lista:
    print(y)


# In[4]:


len(lista)
print("El resultado de la suma de los elemtnos de la serie es el siguiente:")
suma=0
for z in lista:
 suma += z
 print (suma)

