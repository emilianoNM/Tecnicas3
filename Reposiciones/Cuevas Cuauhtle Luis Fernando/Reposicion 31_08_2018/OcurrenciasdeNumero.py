#Este programa cuenta el numero de ocurrencias de un numero en un arreglo

def NumerodeOcurrencias(nums):
  Contador = 0  
  for Numero in nums:
    if Numero == 6:
      Contador = Contador + 1

  return Contador


print(NumerodeOcurrencias([1, 4, 6, 2, 4, 5, 6, 7, 8, 4, 2, 5, 7, 4]))
print(NumerodeOcurrencias([1, 4, 6, 4, 7, 4, 7, 8, 9, 6, 4, 5, 6, 6, 7, 9, 0]))


