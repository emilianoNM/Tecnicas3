
# coding: utf-8

# In[1]:


print("Bienvenido a la calculadora creada por Ricardo Vilchis Tomás")
print("Es muy simple pero espero que pueda resolver las operaciones que necesites :D")


# In[2]:


def Menu_Principal():
    print("Presione 1 si la operacion que desea realizar es SUMA")
    print("Presione 2 si la operacion que desea realizar es RESTA")
    print("Presione 3 si la operacion que desea realizar es MULTIPLICACION")
    print("Presione 4 si la operacion que desea realizar es DIVISION")
    print("Presione 5 si desea salir de la calculadora")
    Opcion=int(input("Seleccione la operacion que se desea realizar"))
    while (Opcion>0 and Opcion<6):
        if(Opcion==1):
            print("USTED SUMARA DOS NUMEROS")
            print("Digite el primer numero que se va a operar")
            a=int(input())
            print("Digite el segundo numero que se va a operar")
            b=int(input())
            suma=a+b
            print("El resultado de la suma es:",suma)
            Opcion=int(input("Seleccione la operacion que se desea realizar"))
        elif(Opcion==2):
            print("USTED RESTARA DOS NUMEROS")
            print("Digite el primer numero que se va a operar")
            a=int(input())
            print("Digite el segundo numero que se va a operar")
            b=int(input())
            resta=a-b
            print("El resultado de la resta es:",resta)
            Opcion=int(input("Seleccione la operacion que se desea realizar"))
        elif(Opcion==3):
            print("USTED MULTIPLICARA DOS NUMEROS")
            print("Digite el primer numero que se va a operar")
            a=int(input())
            print("Digite el segundo numero que se va a operar")
            b=int(input())
            multiplicacion=a*b
            print("El resultado de la multiplicacion es:",multiplicacion)
            Opcion=int(input("Seleccione la operacion que se desea realizar"))
        elif(Opcion==4):
            print("USTED DIVIDIRA DOS NUMEROS")
            print("Digite el primer numero que se va a operar")
            a=int(input())
            print("Digite el segundo numero que se va a operar")
            b=int(input())
            division=a/b
            if(division==(a/b)):
                print("El resultado de la division es:",division)
                Opcion=int(input("Seleccione la operacion que se desea realizar"))
        elif(Opcion==5):
            print("GRACIAS POR HABER USADO LA CALCULADORA ESPERO LE HAYA SERVIDO, VUELVA PRONTO :D")
            return "Bye :)"
            
            


# In[3]:


Menu_Principal()

