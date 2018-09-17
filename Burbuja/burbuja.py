def burbuja(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1][1] < A[j][1]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
    print A;

A=[['Asimov',300],['Parrot',500],['Syma',200],['Adata',800],['Sandisk',250],['Casio',200],['Xiami',550],['HP',695],['Autel',25],['Holy Stone',69],['Yuneec',250],['DJI',666]]
print len(A)
burbuja(A)
