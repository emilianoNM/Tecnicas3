
# coding: utf-8

# In[1]:


#Ordenamiento burbuja
#Por CBLUELENNON (RVT)


# In[2]:


def OrdBurbuja(NombreEMP):
    for i in range(1,len(NombreEMP)):
        for j in range(0,len(NombreEMP)-i):
            if(NombreEMP[j+1] < NombreEMP[j]):
                aux=NombreEMP[j];
                NombreEMP[j]=NombreEMP[j+1];
                NombreEMP[j+1]=aux;
    print (NombreEMP);
 
#Una vez definida la funcion solamente hay que aplicarla a una lista de elementos invocandola paa verla en accion :D
NombreEMP=["Sony","Movistar","Asimov","LALA","Bungie","Burguer King"]
print (NombreEMP)
OrdBurbuja(NombreEMP);

