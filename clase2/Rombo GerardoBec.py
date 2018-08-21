
# coding: utf-8

# In[ ]:


def imprimirRombo(n):
    n = n//2
    for i in range(n,0,-1):
        for j in range(n,(n-(i+1)),-1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print
    for i in range(0,n):
        for j in range(n,(n-(i+1)),-1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print 
 
imprimirRombo(10)

