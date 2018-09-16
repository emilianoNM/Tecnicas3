A = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

B = [[12,45,32],
    [35,98,1],
    [42,43,90]]

resultado = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(A)):

   for j in range(len(A[0])):
       resultado[i][j] = A[i][j] + B[i][j]

for r in resultado:
   print(r)
