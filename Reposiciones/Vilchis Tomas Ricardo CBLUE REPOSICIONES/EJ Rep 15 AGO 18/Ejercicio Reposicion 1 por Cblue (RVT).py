
# coding: utf-8

# In[1]:


#Ejercicio de reposicion 1
#Impresion de una figura con "*"" Creado por Cblue (RVT)


# In[2]:


print("Bienvenido al programa para crear un rectangulo de x*y el rctangulo estara sobreado por * " )
print("Ingresa primero el numero de columnas que quieres que tenga el Rectangulo/Cuadrado y luego el numero de filas")
x=int(input("Columnas"))
y=int(input("Filas"))

for i in range(1,x+1): #Esto se hace porque en FOR el ciclo acaba un termino antes del que queremos o coloquemos en el FOR
    for j in range (1,y+1):
        print("*", end="") #El end es para que siga imprimiendo * en una linea y no se salte a la siguiente despues de haber impreos el primer asterisco
    print(" ")

