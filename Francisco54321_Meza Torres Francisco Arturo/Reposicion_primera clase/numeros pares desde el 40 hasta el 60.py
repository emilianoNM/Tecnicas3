###Imprimir los numeros pares desde el 40 hasta el 60, ambos inclusive
n = 40
h = ''
while n <= 60:
    if n%2 == 0:
        h += ' %i' % n
    n += 1
print h
