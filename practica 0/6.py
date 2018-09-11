

print("PachecoJesus")def serie():
    end = 0
    suma = 0
    conde = 0
    while end <= 1800:
        print(end)
        suma += end
        if conde%2 == 0:
            end += 2
        else:
            end +=3
        conde += 1
    print("La suma de la serie es: ", suma)
serie()