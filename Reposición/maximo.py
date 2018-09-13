def max_de_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n1 and n3 > n2:
        print n3
    else:
        print "Son iguales"
