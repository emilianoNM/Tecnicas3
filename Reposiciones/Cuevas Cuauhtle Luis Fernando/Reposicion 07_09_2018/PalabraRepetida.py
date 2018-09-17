#Programa para identificar si existe una palabra repetida

def PalabraRepetida(str1):
  temp = set()
  for Palabra in str1.split():
    if Palabra in temp:
      return Palabra;
    else:
      temp.add(Palabra)
  return 'No hay palabra repetida'
print(PalabraRepetida("ab ca bc ab"))
print(PalabraRepetida("ab ca bc ab ca ab bc"))
print(PalabraRepetida("ab ca bc ca ab bc"))
print(PalabraRepetida("ab ca bc"))
