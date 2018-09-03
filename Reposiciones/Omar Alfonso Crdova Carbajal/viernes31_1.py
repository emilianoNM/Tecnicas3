import math
import random


def listaAleatorios(n):
    lista = [0] * n
    for i in range(1, n):
        lista[i] = random.random()
    return lista


def hIzq(i):
    return 2 * i


def hDer(i):
    return 2 * i + 1

def intercambia(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def MaxHeapify(A, i, tamanoHeap):
    L = hIzq(i)
    R = hDer(i)
    if (L <= tamanoHeap and A[L] > A[i]):
        posMax = L
    else:
        posMax = i
    if (R <= tamanoHeap and A[R] > A[posMax]):
        posMax = R
    if (posMax != i):
        intercambia(A, i, posMax)
        MaxHeapify(A, posMax, tamanoHeap)

def construirHeapMaxIni(A, tamanoHeap):
    for i in range(math.ceil(tamanoHeap / 2) - 1, 0, -1):
        MaxHeapify(A, i, tamanoHeap)


def OrdenacionHeapSort(A, tamanoHeap):
    construirHeapMaxIni(A, tamanoHeap)
    for i in range(len(A[1:]), 1, -1):
        intercambia(A, 1, i)
        tamanoHeap = tamanoHeap - 1
        MaxHeapify(A, 1, tamanoHeap)


lista = [0, 2, 8, 7, 1, 3, 5, 6, 4]
print("Lista sin ordenar:", lista[0:])
OrdenacionHeapSort(lista, len(lista) - 1)
print("Lista ordenada:", lista[0:])
listaAleatoria = listaAleatorios(6)
print("\nLista aletoria:", listaAleatoria[0:])
OrdenacionHeapSort(listaAleatoria, len(listaAleatoria) - 1)
print("Lista ordenada:", listaAleatoria[0:])
