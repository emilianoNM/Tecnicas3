

print("PachecoJesus")

X=[1,1.8,2.0,2.5,3,5,15.3]
Y=[1,1.5,2.5,2.8,4,6,17.8]

def reg(a, b):
    A=0; B=0; C=0; D=0; E=0;
    for i in range(0, len(a)):
        A=A+a[i] 
        B=B+(a[i])**2
        C=C+b[i]
        D=D+(b[i])**2
        E=E+(b[i])*(a[i])

    m=(C*B-A*E)/(7*B-A*A)
    n=(len(a)*E-A*C)/(7*B-A*A)
    print("La recta es: ",n, "x + ",m )

reg(X,Y)