#Programa que determina si el alumno a aprobado o no
#Chavez Granados Carina

nota1 = float(input("Ingrese la calificacion obtenida en el primer parcial "))
nota2 = float(input("Ingrese la calificacion obtenida en el segundo parcial "))
nota3 = float(input("Ingrese la calificacion obtenida en el tercer parcial "))
puntosExtra = float(input("Ingrese puntos extra sobre calificacion final. De no tener ingrese 0 "))
calificacion = ((nota1+nota2+nota3)/3)+ puntosExtra
if(calificacion ==0 or calificacion > 10):
    print ("Nota invalida")
elif (calificacion <= 5.9):
    print ("Estudiante Reprobado")
elif(calificacion >= 6):
    print ("Estudiante Aprobado")
else:
    print ("Nota registrada")
