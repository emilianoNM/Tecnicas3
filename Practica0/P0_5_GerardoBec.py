
# coding: utf-8

# In[10]:


print("GerardoBec")
def Menu():
    print("1. Capturar Matriz 2x2")
    print("2. Mostrar Matriz")
    print("3. Mostrar Traspuesta")
    print("4. Calcular la Traza")
    print("5. Calcular el Determinante")
    print("6. Salir")
    Opcion=int(input("Seleccione que desea hacer: "))
    traza = 0
    det = 0
    while (Opcion>0 and Opcion<7):
        if(Opcion==1):
            a=(input("Ingresa primer elemento: "))
            b=(input("Ingresa segundo elemento: "))
            c=(input("Ingresa tercer elemento: "))
            d=(input("Ingresa cuarto elemento: "))
            m = [[a,b],[c,d]]
            Opcion=int(input("Seleccione que desea hacer: "))
        elif(Opcion==2):
            print("Matriz: ")
            print (m)
            Opcion=int(input("Seleccione que desea hacer: "))
        elif(Opcion==3):
            print("La transpuesta de la matriz es: ")
            t = [[a,c],[b,d]]
            print (t)
            Opcion=int(input("Seleccione que desea hacer: "))
        elif(Opcion==4):
            traza = (a+d)
            print("La traza de la matriz es: ", traza)  
            Opcion=int(input("Seleccione que desea hacer: "))
        elif(Opcion==5):
            det = ((a*d)-(b*c))
            print("El determinante de la matriz es: ", det)
            Opcion=int(input("Seleccione que desea hacer: "))
        elif(Opcion==6):
            return


# In[11]:


Menu()

