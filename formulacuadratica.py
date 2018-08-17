A=input("da valor de a")
B=input("da valor de b")
C=input("da valor de c")


print(A,"*x^2+", B ,"*x+",C)
x_1=(-B+(B^2-4*A*C)^(1/2))/2*A
x_2=(-B-(B^2-4*A*C)^(1/2))/2*A
print(x_1,x_2)
