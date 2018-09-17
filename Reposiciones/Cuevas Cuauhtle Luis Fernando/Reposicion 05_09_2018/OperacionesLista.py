"""Este programa hace varias operaciones con una lista como la suma de sus elementos, la
multi;licacion entre ellos, y te dice cual es el mayor y el menor"""



def SumaLista(items):
    Numeros = 0
    for x in items:
        Numeros += x
    return Numeros
print("La suma de los elementos de la lista es:",SumaLista([1,2,-8]))

def MultiplicacionLista(items):
    Numero = 1
    for x in items:
        Numero *= x
    return Numero
print("La multiplicacion de los elementos de la lista es:",MultiplicacionLista([1,2,-8]))

def NumeroMayor( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print("El numero mayor de los elementos de la lista es:",NumeroMayor([1, 2, -8, 0]))