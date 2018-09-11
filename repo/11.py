
#Pacheco Rios Jes{us}
def main():
print "Convierte medidas inglesas a sistema metrico"
millas = input("Ingrese las  millas ")
pies = input(" Ingrese cuantos pies: ")
pulgadas = input("Ingrese el numero de pulgadas: ")

metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
print "La longitud es de ", metros, " metros"
main()