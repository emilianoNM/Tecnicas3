print 'Linares Alonso Joshua A. '
print "impresion de un ovalo"

m=9
n=7

for i in range(1,m+1):

  if (i==1 or i==m):
    for j in range(2,n+1):
      if (j>=4 and j<=6):
        print "*",
      else:  
        print " ",    


  if(i==2 or i==m-1):
    for j in range(2,n+1):
      if (j==3 or j==7):
        print "*",   
      else:
        print " " ,    

  if(i>2 and i<=m-2):
      print "*",
      for j in range (2,n+1):
        if(j==n):
          print "*",
        else:
          print " ",  


  print (" ")  


