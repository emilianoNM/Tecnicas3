door=True
Matriz=[]
while(door):
    print("1)Capturar Nueva Matriz")
    print("2)Imprimir Matriz")
    print("3)Transpuesta")
    print("4)Traza")
    print("5)Determinante")
    print("6)Salir")

    choice=int(input("Eliga Opcion"))

    if(choice==1):
        del Matriz[:]
        for i in range(0, 4):
            Matriz.append(int(input("Ingrelos elementos")))

    if (choice == 2):
        print(Matriz[0], Matriz[1])
        print(Matriz[2], Matriz[3])

    if (choice == 3):
        print(Matriz[0], Matriz[2])
        print(Matriz[1], Matriz[3])

    if (choice==4):
        print(Matriz[0]+Matriz[3])

    if (choice==5):
        print(Matriz[0]*Matriz[3]-Matriz[1]*Matriz[2])

    if(choice==6):
        door=False




