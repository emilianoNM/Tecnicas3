print " Linares Alonso Joshua A."
print "impresion de una flecha hacia la derecha"
m=5
n=9
for i in range(1,m+1):
  if(i==1 or i==5):
     for j in range(1,n+1):
       if(j==7):
         print "*",
       else:
        print " ",

  if(i==2 or i==4):
    for j in range(1,n+1):
       if(j==7 or j==8):
           print "*",   
       else:
             print " ",   

  if(i==3):
    for j in range(1,n+1):
           print "*",   

  
  print (" ")  
