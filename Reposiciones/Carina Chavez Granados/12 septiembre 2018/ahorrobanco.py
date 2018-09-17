#Programa que calcula el ahorro que logra acumular una persona en un banco en un anio
#Chavez Granados Carina

n = int(input("Ingrese el deposito inicial: "))
tasainteres = int(input("Ingrese el porcentaje de tasa de interes: "))
x = 1
total = 0
while x <= 24:
    gananciaMes =  n*tasainteres/100
    total = total + gananciaMes
    x = x+1
print("El ingreso inicial %d de sus intereses %d son: %5.2f" % (n, tasainteres, total))
