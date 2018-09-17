#Calculadora con Suma, Resta, Multiplicacion b Division
print("\nResolucion a Problema 2.16 del Libro Deitel H.M C++ How to Program 10th Edition\n\n")
print("""(Arithmetic) Write a program that asks the user to enter two numbers, obtains the two
numbers from the user and prints the sum, product, difference, and quotient of the two numbers.""")
print (" \n\t\t\tCalculadora\n")
print('\t\t    Operaciones Basicas\n\n')



def Menu():

    print (""" Eliga una opcion

\tMenu

[1] Suma
[2] Resta
[3] Multiplicacion
[4] Division
[5] Salir\n\n""")

def Operaciones():

    Menu()

    Opcion = int(input("Eliga una opcion\n"))

    while (Opcion >0 and Opcion <5):
        a = int(input("Ingrese el primer numero\n"))
        b = int(input("Ingrese el segundo numero\n"))
        if (Opcion==1):
            print ("El resultado de la suma es:", a+b)
            Opcion = int(input("Selecione Opcion\n"))
        elif(Opcion==2):
            print ("El resultado de la resta es:",a-b)
            Opcion = int(input("Selecione Opcion\n"))
        elif(Opcion==3):
            print ("El resultado de la multiplicacion es:",a*b)
            Opcion = int(input("Selecione Opcion\n"))
        elif(Opcion==4):
            try:
              print ("El resultado de la division es:", a/b)
              Opcion = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              Opcion = int(input("Selecione Opcion\n"))
Operaciones()