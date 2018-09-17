##Imprimir los numeros del 1 al 100 y calcular la suma de todos los nuumeros 
###pares por un lado, y por otro, la de los impares.
n = 1
p = 0
i = 0
while n <= 100:
    print n,
    if n%2 == 0:
        p += n
    else:
        i += n
    n += 1
print '\nLa suma de los pares es igual a %i' % p
print 'La suma de los impares es igual a %i' % i
