
# coding: utf-8

# In[ ]:


def superpisicion(lista1,lista2):
    indice=0
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

a=[1,2,3]
b=[4,5,6,7,3]

print superposicion (a,b)
 


