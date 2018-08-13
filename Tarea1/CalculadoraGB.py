# In[2]:
def Menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    Opcion=int(input("Seleccione la operacion que se desea realizar  "))
    while (Opcion>0 and Opcion<6):
        if(Opcion==1):
            print("Primer numero a operar")
            a=int(input())
            print("Segundo numero a operar")
            b=int(input())
            suma=a+b
            print("El resultado de la suma es:",suma)
            Opcion=int(input("Seleccione la operacion que se desea realizar  "))
        elif(Opcion==2):
            print("Primer numero a operar")
            a=int(input())
            print("Segundo numero a operar")
            b=int(input())
            resta=a-b
            print("El resultado de la resta es:",resta)
            Opcion=int(input("Seleccione la operacion que se desea realizar  "))
        elif(Opcion==3):
            print("Primer numero a operar")
            a=int(input())
            print("Segundo numero a operar")
            b=int(input())
            multiplicacion=a*b
            print("El resultado de la multiplicacion es:",multiplicacion)
            Opcion=int(input("Seleccione la operacion que se desea realizar  "))
        elif(Opcion==4):
            print("Primer numero a operar")
            a=int(input())
            print("Segundo numero a operar")
            b=int(input())
            division=a/b
            print("El resultado de la division es:",division)
                Opcion=int(input("Seleccione la operacion que se desea realizar  "))
        elif(Opcion==5):
            return 

