
# coding: utf-8

# In[ ]:



def insertarElemento(lista, indice, elemento):
    lista.insert(indice,elemento)
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
 
    i=0
    while i < 10:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
imprimirLista(A,"A")
cn_val=int(raw_input("Ingrese Valor: "))
cn_ind=int(raw_input("Ingrese Indice: "))
insertarElemento(A,cn_ind,cn_val)
imprimirLista(A,"A")

