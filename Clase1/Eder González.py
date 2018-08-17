
# coding: utf-8

# In[1]:


frase = input('Ingrese una frase:') 
 
temp = frase.replace(' ','') 
 
if temp == temp[::-1]: 
    print('La frase es palindromo') 
else: 
    print('No es palindromo') 

