
#Pacheco Rios Jes{us}
def main():
f = input("¿Cuánto cuesta 1 segundo de comunicacion?: ")
n = input("¿Cuántas llamadas se hicieron ?:")
for x in range(n):

  h = input("¿Cuantas horas?: ")
  m = input("¿Cuantos minutos?: ")
  s = input("¿Cuantos segundos?: ")

  calculo = asegundos(h, m, s)

  costo = calculo * f
  print "Duracion: ", calculo, "segundos. Costo: ",costo, "$."

def asegundos (h, m, s):
  segsal = 3600 * h + 60 * m + s
  return segsal