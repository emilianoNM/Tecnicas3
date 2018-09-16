print " Linares Alonso Joshua A."
print "impresion de una flecha hacia abajo"
m=9
n=5
for i in range(1,m+1):
  if(i==9):
     for j in range(1,n+1):
       if(j==3):
         print "*",
       else:
        print " ",

  if(i==8):
    for j in range(1,n+1):
       if(j>=2 and j<=4):
           print "*",   
       else:
             print " ",   

  if(i==7):
    for j in range(1,n+1):
           print "*",   

  if(i<=6):  
    for j in range(1,n+1):
       if(j==3):
         print "*",
       else:
        print " ",   

  print (" ")  
