
# coding: utf-8

# In[1]:


print("Bienvenido al programa para convertir de grados Kelvin a Fahrenheit creado por Ricardo Vilchis")


# In[2]:


def Convertidor():
    gradoskelvin=int(input("Ingrese los grados Kelvin de su medicion o los que le interesa convertir a grados Fahrenheit mi estima@"))
    while(gradoskelvin>=-1001 and gradoskelvin<=1001):
        gradosF=(9/5)*(gradoskelvin-273.15)+32
        print(gradoskelvin," Grados Kelvin son en escala Fahrenheit", gradosF, "Grados Fahrenheit")
        NuevaOpcion=input("¿Desea convertir de nuevo? Ingrese 'si' para volver a convertir o 'no' para salir del convertidor")
        if(NuevaOpcion=="si"):
            gradoskelvin=int(input("Ingrese los grados Kelvin de su medicion o los que le interesa convertir a grados Fahrenheit mi estimad@"))
        elif(NuevaOpcion=="no"):
            return 'BYE VUELVE PRONTO BESOS TQM'


# In[3]:


Convertidor()

