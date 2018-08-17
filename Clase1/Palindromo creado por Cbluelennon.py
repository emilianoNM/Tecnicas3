
# coding: utf-8

# In[1]:


string=input("Dame el palindromo que deseas comprobar :) \n")


# In[2]:


print(string.replace(' ', '')==string.replace(' ','')[::-1])

