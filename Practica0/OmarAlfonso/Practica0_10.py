import math
x=1
i=0
Error=1000
while Error>.01:
    y = -math.log(x)+math.exp(-x)
    dy=-math.exp(-x)- 1/x
    x1=x-y/dy
    Error=abs((x-x1)/(x1))
    x=x1
    i=i+1
    print(i,x,y,Error)