import random
def BusquedaLineal(A, n, x):
   iteracion1 = 0
   encontrado = -1
   for k in range(n):
       iteracion1 = iteracion1 + 1
       if (x == A[k]):
           encontrado = k
   print("Número de iteraciones:", iteracion1)
   return encontrado


def BusquedaLinealMejorado(A, n, x):
   iteracion2 = 0
   encontrado = -1
   for k in range(n):
       iteracion2 = iteracion2 + 1
       if A[k] == x:
           encontrado = k
           print("Número de iteraciones:", iteracion2)
           break
   if encontrado == -1:
       print("Número de iteraciones:", iteracion2)
   return encontrado


def BusquedaLinealCentinela(A, n, x):
   iteracion3 = 0
   tmp = A[n - 1]
   A[n - 1] = x
   k = 0
   while (A[k] != x):
       iteracion3 = iteracion3 + 1
       k = k + 1
   A[n - 1] = tmp
   if (k < n - 1 or A[n - 1] == x):
       print("Número de iteraciones:", iteracion3)
       return k
   else:
       print("Número de iteraciones:", iteracion3)
       return -1


# Prueba
print("Creando lista aleatoria:\n")
A = []
for i in range(100):
   A.append(random.randint(1, 1000))
print(A)
print("\nNúmero a buscar es", A[50], "por lo que el índice que regresan los algoritmos debe de ser 50\n")
i = BusquedaLineal(A, 100, A[50])
if i != -1:
   print("El índice de 765 es:", i, "\n")
else:
   print("Número no encontrado\n")
i = BusquedaLinealMejorado(A, 100, A[50])
if i != -1:
   print("El índice de 765 es:", i, "\n")
else:
   print("Número no encontrado\n")
i = BusquedaLinealCentinela(A, 100, A[50])
if i != -1:
   print("El índice de 765 es:", i, "\n")
else:
   print("Número no encontrado\n")
