
# coding: utf-8

# In[1]:


#Programa que suma dos matrices ya preestablecidas
#Cbluelennon (RVT)


# In[2]:


#La mtariz ya esta preestablecida pero se pueden acomodar valores que se deseen o ir ingresando elemento por elemento
#en cada una de las dos matrices agregando algunas lineas de codigo extra
M = [
 [2, 3, 4],
 [6, 4, 3],
 [1, 4, 6],
]

N = [
 [2, 1, 7],
 [6, 9, 9],
 [1, 5, 8],
]

s=[[M[i][j]+N[i][j]
for j in range(len(M))] 
for i in range(len(N))]
print(s)

