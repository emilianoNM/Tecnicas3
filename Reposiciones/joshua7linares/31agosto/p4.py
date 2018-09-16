print " Linares Alonso Joshua A."
print "impresion de una flecha"
m=9
n=5

for i in range(1,m+1):
  if(i==1):
     for j in range(1,n+1):
       if(j==3):
         print "*",
       else:
        print " ",
        
  if(i==2):
    for j in range(1,n+1):
       if(j>=2 and j<=4):
           print "*",   
       else:
             print " ",   

  if(i==3):
    for j in range(1,n+1):
           print "*",   

  if(i>=4):  
    for j in range(1,n+1):
       if(j==3):
         print "*",
       else:
        print " ",   

  print (" ")  
