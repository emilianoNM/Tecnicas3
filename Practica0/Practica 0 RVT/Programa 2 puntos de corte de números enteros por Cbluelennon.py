
# coding: utf-8

# In[1]:


print("Bienvenido al programa para clasificar numeros ENTEROS")
print("Ingresara 10 numeros para su posterior clasificacion\n")
print("El programa los clasificara entre numeros pares o impares\n")


# In[2]:


lista=[]
print("Ingresa los 10 numeros que el programa clasificara")
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))


# In[3]:


i=0
j=0
listapares=[]
listaimpares=[]
while(i>=0 and i<=9):
    if(lista[j]%2==0):
        listapares.append(lista[j])
    elif(lista[j]%2!=0):
        listaimpares.append(lista[j])
    j=j+1
    i=i+1


# In[4]:


print("Los numeros pares son:")
for x in listapares:
    print (x)
print("Los numeros impares son:")
for y in listaimpares:
    print(y)

