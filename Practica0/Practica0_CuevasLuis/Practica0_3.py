#Es necesario Instalar las librerias Pip y Numpy para correr este programa

import numpy as np

def Menu():

    print """ Operaciones Matriciales

\t\tMenu

[1] Anadir elementos a la Matriz
[2] Imprimir Matriz
[3] Transponer Matriz
[4] Calcular su Traza
[5] Calcular su Determinante 
[0] Salir del Programa


"""
def Matriz():
    print "\n\nSeleccione una Opcion y presione ENTER\n\n"

    Menu()
    Opcion = int(input("Selecione alguna Opcion\n"))

    while (Opcion >0 and Opcion <6):

        if (Opcion==1):

	      Elemento11 = int(input("Primer numero:"))
	      Elemento12 = int(input("Segundo numero:"))
              Elemento21 = int(input("Tercer numero"))
              Elemento22 = int(input("Cuarto numero"))

              Matriz = np.array([[Elemento11, Elemento12],
              		    [Elemento21, Elemento22]])

        elif(Opcion==2):

            print Matriz
           
        elif(Opcion==3):

            Transpuesta=np.transpose(Matriz)

	    print Transpuesta

        elif(Opcion==4):

           Traza=np.trace(gi)

	   print Traza
          
        elif(Opcion==5):

            Transpuesta=np.linalg.det(Matriz)

	    print Transpuesta

	elif(Opcion==6):

	    Opcion=-1
              
	Opcion = int(input("Selecione Opcion\n"))
	
Matriz()