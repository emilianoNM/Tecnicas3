

import random
def listaAleatorios(n):
    lista = [0] * n
    for i in range(1, n):
        lista[i] = random.random()
    return lista

def intercambia(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def Particionar(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if (A[j] <= x):
            i = i + 1
            intercambia(A, i, j)
            intercambia(A, i + 1, r)
    return i + 1


def QuickSort(A, p, r):
    if (p < r):
        q = Particionar(A, p, r)
        print(A[p:q], "{", A[q:q + 1], "}", A[q + 1:r + 1])
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)


lista = [0, 2, 8, 7, 1, 3, 5, 6, 4]
print("Lista sin ordenar:", lista[1:])
print("{[n]} es el pivote\n")
QuickSort(lista, 1, 8)
print("Lista ordenada:", lista[1:])
listaAleatoria = listaAleatorios(6)
print("\nLista aletoria", listaAleatoria[1:])
print("-[n]- es el pivote\n")
QuickSort(listaAleatoria, 1, 5)
print("Lista ordenada:", listaAleatoria[1:])
