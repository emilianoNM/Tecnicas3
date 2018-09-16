print "Linares Alonso Joshua A."
print "impresion del contorno de un rectangulo con asteriscos"

m=int(input("numero de renglones: "))
n=int(input("numero de columnas: "))

for i in range(1,m+1):
  if (i==1 or i==m):
     for j in range(1,n+1):
       print "*",    

  if(i>1 and i!=m):
      print "*",
      for j in range (2,n+1):
        if(j==n):
          print "*",
        else:
          print " ",  

  print (" ")
