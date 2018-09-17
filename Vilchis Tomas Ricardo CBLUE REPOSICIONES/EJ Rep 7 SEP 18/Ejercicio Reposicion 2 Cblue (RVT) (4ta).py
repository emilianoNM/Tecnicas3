
# coding: utf-8

# In[1]:


#Programa que identifique si un numero es primo o no lo es
#Programa creado por CBLUELENNON (RVT)


# In[2]:


for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
 
while True:
    try:
        numero = int(raw_input("inserta un numero (0) salir >> "))
        if numero==0:
            break
        if es_primo(numero):
            print ("\nEl numero %s es primo" % numero)
        else:
            print ("\nEl numero %s NO es primo" % numero)
    except:
        print ("\nEl numero tiene que ser entero")

