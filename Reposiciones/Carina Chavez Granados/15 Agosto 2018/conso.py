#Programa que imprime solo consonantes de una cadena
def consonantes(cadena):
	lista=""
	for vo in cadena:
		if vo=='a' or vo=="e" or vo=="i" or vo=="o" or vo=="u"  or vo=="A" or vo=="E" or vo=="I" or vo=="O" or vo=="U":
			pass
		else:
			lista+=vo
	return lista
cadena=raw_input("Ingrese una frase: ")
print (consonantes(cadena))
