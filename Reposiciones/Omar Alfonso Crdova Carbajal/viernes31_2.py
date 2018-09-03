def CountingSort(A, k):
   # crea arreglos C y B
   C = [0 for _ in range(k + 1)]
   B = [0 for _ in range(len(A))]
   for j in range(1, len(A)):
       C[A[j]] = C[A[j]] + 1
   for i in range(1, k + 1):
       C[i] = C[i] + C[i - 1]
   for j in range(len(A) - 1, 0, -1):
       B[C[A[j]]] = A[j]
       C[A[j]] = C[A[j]] - 1
   return B


lista1 = [0, 2, 5, 3, 0, 2, 3, 0, 3]
lista2 = [0, 45, 100, 1, 5, 9, 10, 12, 3]
lista3 = [0, 9, 21, 4, 40, 10, 35]
print("Lista vista en clase(L1):", lista1)
print("Lista propuesta(L2):", lista2)
print("Lista designada(L3):", lista3)
lista1 = CountingSort(lista1, 5)
print("\nL1: ", lista1)
lista2 = CountingSort(lista2, 100)
print("L2:", lista2)
lista3 = CountingSort(lista3, 40)
print("L3:", lista3)

