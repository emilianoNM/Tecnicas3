###Programa que imprima los nuumeros impares desde el 100 hasta la unidad y calcule su suma
n = 100
h = 0
while n >= 1:
    if n%2 != 0:
        print n,
        h += n
    n -= 1
print 'y su suma es: %i' % h
