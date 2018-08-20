lado = int(input("Introduce longitud: "))

for x in list(range(lado)) + list(reversed(range(lado-1))):
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1=lado-x-1, w2=x*2+1))

