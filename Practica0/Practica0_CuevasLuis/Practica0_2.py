#Busqueda de Ocurrencias de una palabra en un texto

print("Programa contador de ocurrencias de una cierta palabra en un Texto")
Oracion=raw_input("Introduce tu frase/Oracion/Texto:")
Palabra=raw_input("Introduce la palabra a contar sus ocurrencias:")
ArregloPalabras=[]
conteo=0
ArregloPalabras=Oracion.split(" ")
for i in range(0,len(ArregloPalabras)):
      if(Palabra==ArregloPalabras[i]):
            conteo=conteo+1
print("El numero de veces que aparece la palabra son")
print(conteo)