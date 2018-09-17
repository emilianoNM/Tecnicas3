#Este Programa calcula el area de un triangulo y lo imprime en pantalla

Base = int(input("Intruduzca la base del Triangulo: "))
Altura = int(input("Intruduzca la Altura del Triangulo: "))

area = Base*Altura/2

print("El area es = ", area)
     
for i in range(1,Altura+1):
    print ((Altura-i)*' '+i*'* ')