x0=int(input("ingrese un Numero entero"))
x1=int(input("ingrese un Numero entero"))
A=[]
B=[]
C=[]

for i in range (0,10):
    x=int(input("Ingrese Entero"))
    if x0>x1:
        t=x0
        x0=x1
        x1=t

    if x<x0:
        A.append(x)
    if x>x1:
        C.append(x)
    else:
        B.append(x)
print(A, "<", x0,"<", B,"<", x1, "<", C)




