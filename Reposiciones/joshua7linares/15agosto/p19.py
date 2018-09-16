
def num(n,m):
  for i in range(n,m+1):
    l=dp(i,m+1)
    e=dp2(i,m+1)
    f=dp3(i,m+1)
    print i," "," "," ",l," "," "," "," ",e," "," "," "," ",f

def dp(n,m):
  for i in range(n,m+1):
    return i*10

def dp2(n,m):
  for i in range(n,m+1):
    return i*100

def dp3(n,m):
  for i in range(n,m+1):
    return i*1000        

n=input("limite inferior: ")
m=input("limite superior: ")
print "N"," ", " ","10  *  N"," "," ","100  *  N"," "," " "1000  *  N"
num(n,m) 
