#En este programa se imprime la Serie de Fibonacci con respecto a un intervalo


Elemento1,Elemento2=0,1

Fin = int(input("\nIntroduzca el numero limite de la Serie de Fibonacci:\t"))

while Elemento2<Fin:

    print(Elemento2)

    Elemento1,Elemento2 = Elemento2,Elemento1+Elemento2
