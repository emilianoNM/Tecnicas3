###Imprimir los numeros impares desde el 1 al 25, ambos inclusive
n = 1
h = ''
while n <= 25:
    if n%2 != 0:
        h += ' %i' % n
    n += 1
print h
