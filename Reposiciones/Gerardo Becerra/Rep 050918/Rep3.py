
# coding: utf-8

# In[ ]:


#GerardoBecerra

def superposicion (Lista1, lista2):
    indice =0
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
        return False
    
a=[1,2,3,4]
b=[5,6,7,8,9,]

print superposicion (a,b)

