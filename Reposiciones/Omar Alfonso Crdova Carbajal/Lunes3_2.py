import math
import random

def intercambia(A,x,y):
   tmp=A[x]
   A[x]=A[y]
   A[y]=tmp
def Particionar(A,p,r):
   x=A[r]
   i=p-1
   for j in range(p,r):
       if (A[j]<=x):
           i=i+1
           intercambia(A,i,j)
   intercambia(A,i+1,r)
   return i+1
def QuickSort(A,p,r):
   if (p<r):
       q=Particionar(A,p,r)
       QuickSort(A,p,q-1)
       QuickSort(A,q+1,r)
   return A

def BusquedaBinariaIterativa(A,x,indiceIzq,indiceDer):
   while(indiceIzq<=indiceDer):
       medio=math.floor((indiceIzq+indiceDer)/2)
       if (x==A[medio]):
           return medio
       elif(A[medio]<x):
           indiceIzq=medio+1
       else:
           indiceDer=medio-1
   return -1

def BusquedaBinariaRecursiva(A,x,indiceIzq,indiceDer):
   if(indiceIzq>indiceDer and x!=A[indiceDer]):
       return -1
   medio=math.floor((indiceIzq+indiceDer)/2)
   if(x==A[medio]):
       return medio
   elif(x<A[medio]):
       return BusquedaBinariaRecursiva(A,x,indiceIzq,medio)
   else:
       return BusquedaBinariaRecursiva(A,x,medio,indiceDer)

#Prueba
print("Creando lista aleatoria:\n")
A=[]
for i in range(100):
   A.append(random.randint(1,1000))
print("Lista sin ordenar:",A)
A=QuickSort(A,0,99)
print("\nLista ordenada:",A)
print("\nEl número a buscar es",A[50],"por lo que el índice que regresan los algoritmos debe de ser 50\n")
i=BusquedaBinariaIterativa(A,A[50],0,len(A))
print("El índice (mediante interativa) es:",i)
i=BusquedaBinariaRecursiva(A,A[50],0,len(A))
print("El índice (mediante recursiva) es:",i)
