
print "impresion de triangulos rectangulos invertidos"
n=input("altura: ")
for i in range(n+1):
  if (i==0):
    print ("*"*n)

  else:
    print("*"*(n-i))  



for i in range(n+1):
  if (i==0):
    print ("*"*n)
  else:
    esp=i
    print (" "*esp+"*"*(n-i))  
