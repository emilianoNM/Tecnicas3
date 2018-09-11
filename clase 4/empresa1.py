# coding: utf-8

# In[ ]:


import Empresas
testEmpresa=Empresas.UnidadEconomica('CblueCo','Tecnologica','CblueCo Ingenieria SA De CV')


# In[ ]:


if(testEmpresa.nombre=='CblueCo'):
    print("test de manera correcta")
else():
    print("test de nombre error")

print(testEmpresa.tipo)
print(testEmpresa.razonSocial)