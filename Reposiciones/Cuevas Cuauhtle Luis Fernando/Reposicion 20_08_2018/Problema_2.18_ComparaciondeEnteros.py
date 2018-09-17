#Comparador de dos enteros 

print("\nResolucion a Problema 2.18 del Libro Deitel H.M C++ How to Program 10th Edition\n")


print("""2.18 (Comparing Integers) Write a program that asks the user to enter two integers, obtains the
numbers from the user, then prints the larger number followed by the words "is larger." If the
numbers are equal, print the message "These numbers are equal . "\n\n""")



print("Comparador de Enteros\n\n Porfavor Introduzca dos Numeros (Enteros)")

Salir = 's'

while (Salir == 's') :
	

	a = int(input("Escriba el Primer Numero a comparar:\n"))

	b = int(input("Escriba el Segundo Numero a comparar\n"))

	if (a==b):

		print(a, "y", b, "son iguales")

		pass

	elif (a<b):

		print(b,"es mayor que",a)

		pass

	elif (a>b):

		print(a,"es menor que",b)

		pass

	print("\nDeseas continuar?\n")
	print("[Si]............... s")
	print("[No]............... n")

	Salir = (raw_input)

	