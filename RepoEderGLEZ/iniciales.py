
# coding: utf-8

# In[ ]:


wahio=[i for i in input('texto: ')]
word,a=wahio[0],0
while a<len(wahio):
    if wahio[a]==' ':
        word+=wahio[a+1]
    a+=1
print(word.upper())

