

print("PachecoJesus")

def suma():
    
    i = int(input("Ingrese el numero inicial: "))
    l = int(input("Ingrese el numero limite: "))
    sumatoria = 0
    for x in range(l+1):
        sumatoria += (1/(x+1))
    print ("La sumatoria es: ", sumatoria)
    
suma()