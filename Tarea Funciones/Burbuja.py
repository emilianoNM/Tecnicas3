
# coding: utf-8

# In[ ]:


def burbuja(empresas): 
  temp=0
  for j in range(1,len(empresas)):
    for i in range(0,len(empresas)-j):
      if (empresas[i]>empresas[i+1]):
        temp=empresas[i]
        empresas[i]=empresas[i+1]
        empresas[i+1]=empresas[i]
        empresas[i+1]=temp


print "Ordenamiento"
empresas=["Inspiron","Samsung","Ford","Nike","Puma","Casio","Porrua","ICA FLUOR","Asimov"] 
print empresas
burbuja(empresas)
print "Ordenado: "
print empresas 

