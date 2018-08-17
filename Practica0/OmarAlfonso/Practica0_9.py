X=[1,1.8,2.0,2.5,3,5,15.3]
Y=[1,1.5,2.5,2.8,4,6,17.8]

def Minimos(w, u):
    W=0
    W2=0
    U=0
    U2=0
    WU=0
    for i in range(0, len(w)):
        W=W+w[i] #X
        W2=W2+(w[i])**2 #X
        U=U+u[i]
        U2=U2+(u[i])**2
        WU=WU+(u[i])*(w[i])

    b=(U*W2-W*WU)/(7*W2-W*W)
    m=(len(w)*WU-W*U)/(7*W2-W*W)
    print(m, "x + ",b )

Minimos(X,Y)