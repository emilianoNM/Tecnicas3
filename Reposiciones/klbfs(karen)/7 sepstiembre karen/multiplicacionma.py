X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7,6],
    [5,4,3,2],
    [1,2,3,4]]
resultado = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for l in range(len(Y)):
           resultado[i][j] += X[i][l] * Y[l][j]

for r in resultado:
   print(r)
