
# coding: utf-8

# In[ ]:


def concatenarLista(lista_a, lista_b):
    lista_nueva=[]
 
    for i in range(0,len(lista_a)):
        lista_nueva.append(lista_a[i])
 
    for i in range(0,len(lista_b)):
        lista_nueva.append(lista_b[i])
 
    return lista_nueva
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
 
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 5)))
        i=i+1
    return lista
 
A=leerLista()
B=leerLista()
C=concatenarLista(A, B)
imprimirLista(C,"C")

