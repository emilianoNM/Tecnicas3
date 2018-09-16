print " Linares Alonso Joshua A."
print "impresion de un rectangulo con renglones semivacios"

m=int(input("numero de renglones: "))
n=int(input("numero de columnas: "))

for i in range(1,m+1):
  if(i%2==0):
    for j in range(1,n+1):
      if(j==1 or j==n):
        print "*",
      else:
        print " ",   


  else:  
     for j in range(1,n+1):
       print "*", 

  print (" ")  
