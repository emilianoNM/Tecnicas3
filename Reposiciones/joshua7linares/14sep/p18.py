
def fact(n): 
 factorial=1
 for i in range(n):
   factorial=factorial*n
   n=n-1
 return factorial

print "lista de factoriales"
m=input("limite inferior: ")
k=input("limite superior: ")
print "numero"," " ,"factorial"
for i in range(m,k+1):
  m=fact(i)
  print " ",i," "," "," "," ",m
