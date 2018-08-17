x=0
y=0
i=0
while x<1800:
    i=i+1
    if i%2==0:
        x=x+2

    else:
        x=x+3
    y=y+x
    print(i, x,y)

