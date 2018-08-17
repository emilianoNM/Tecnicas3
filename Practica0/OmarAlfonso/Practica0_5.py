def Resolver(A, B, C):
    x1 = complex((-B + (B**2-4*A*C)**.5)/(2*A))
    x2 = complex((-B - (B ** 2 - 4 * A * C) ** .5) / (2 * A))
    print(x1, x2)

A=complex(input("Ingrese A"))
B=complex(input("Ingrese B"))
C=complex(input("Ingrese C"))

Resolver(A, B,C)



