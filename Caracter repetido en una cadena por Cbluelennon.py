
# coding: utf-8

# In[1]:


print("Programa para contar las veces que un caracter se repite dentro\n de una cadena dada por el usuario, o sea usted :)")


# In[2]:


caracter=str(input("Ingrese un caracter, una letra es recomendable, gracias\n"))
cadena=str(input("Ingrese una cadena de caracteres, una palabra es recomendable, gracias\n"))


# In[3]:


def buscarcaracter():
    i=0
    j=0
    x=0
    while(i>=0 and i<len(cadena)):
        if (cadena[j]==caracter[0]):
            j=j+1
            i=i+1
            x=x+1
        elif(cadena[j]!=caracter[0]):
            j=j+1
            i=i+1
    print("El caracter que ingresaste se repite ",x, "veces en la cadena")
     


# In[4]:


buscarcaracter()

