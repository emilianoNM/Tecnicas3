#Este programa genera numeros aleatorios a partir de una Lista, ya sean palabras o numeros
#Se hara un ejemplo de ambos, generando numeros aleatorias y palabras aleatorias a partir de una lista

import random

ListadeColores = ['Rojo','Azul','Amarillo','Cafe','Verde','Anaranjado','Gris','Negro','Blanco','Morado','']

ListadeNumeros = [1,2,3,4,5,6,7,8,9]

print('\t*Porfavor sigue corriendo el programa para ver la aleatoriedad*')
print("\nColor Aleatorio:")
print(random.choice(ListadeColores))

print("NUmero Aleatorio:")
print(random.choice(ListadeNumeros))
