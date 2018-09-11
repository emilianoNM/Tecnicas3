

print("PachecoJesus")
cadena = (input("Ingrese palabra: "))
carac = (input("Ingrese caracter a buscar: "))
cuenta = 0
for caracter in cadena:
    if caracter == carac:
        cuenta += 1
print ("El numero de veces que se repite la letras es: ") 
print (cuenta)