def menu():
    print "menu calculadora"
    print "opciones:"
    print " "
    print "1) + suma"
    print "2) - resta"
    print "3) x multiplicacion"
    print "4) / division"
    print "5) salir"
    print " "
    return input ("escoge opcion: ")
    
def suma(a,b):
    print a, "+", b, "=", a + b
    
def res(a,b):
    print b, "-", a, "=", b - a
    
def mul(a,b):
    print a, "*", b, "=", a * b
    
def div(a,b):
    print a, "/", b, "=", a / b
    
lala = 1
opcion = 0
while lala == 1:
    opcion = menu()
    if opcion == 1:
        suma(input("SUMA : "),input("A : "))
        lala = 0
    elif opcion == 2:
        res(input("RESTA: "),input("A: "))
        lala = 0
    elif opcion == 3:
        mul(input("MULTIPLICA: "),input("POR: "))
        lala = 0
    elif opcion == 4:
        div(input("DIVIDE: "),input("ENTRE: "))
        lala = 0
    elif opcion == 5:
        lala = 0

print "ADIOS !"
