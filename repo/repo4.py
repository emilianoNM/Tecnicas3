def CrearSubArreglo(A, indIzq, indDer):
    return A[indIzq:indDer + 1]


def Merge(A, p, q, r):
    Izq = CrearSubArreglo(A, p, q)
    Der = CrearSubArreglo(A, q + 1, r)
    print(Izq, "|", Der)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if (j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
            A[k] = Izq[i]
            i = i + 1
        else:
            A[k] = Der[j]
            j = j + 1


def MergeSort(A, p, r):
    if r - p > 0:
        q = int((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


lista = [1, 16, 7, 14, 8, 5]
MergeSort(lista, 0, 5)