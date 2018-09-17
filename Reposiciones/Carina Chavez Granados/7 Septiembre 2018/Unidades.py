#Programa que calcula millares, centenas , decenas y unidades de un numero
#Chavez Granados

def millares(numero):
    return int(numero) / 1000

def centenas(numero):
    return (numero - (millares(numero) * 1000)) / 100

def decenas(numero):
    return (numero - int(millares(numero)*1000 + centenas(numero)*100)) / 10

def unidades(numero):
    return (numero - (millares(numero) * 1000 + centenas(numero) * 100 + decenas(numero) * 10))

def main():

    numero = input("Ingresa el numero que desees descomponer: ")

    print("Los Millares de " + str(numero) + " son: " + str(millares(numero)))
    print("Las Centenas de " + str(numero) + " son: " + str(centenas(numero)))
    print("Las Decenas de " + str(numero) + " son: " + str(decenas(numero)))
    print("Las Unidades de " + str(numero) + " son: " + str(unidades(numero)))


main()
