###programa para saber si un a�o es bisiesto

a=int(input("ingresa a�o\n"))
if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
 print("El a�o "+str(a)+" Si es bisiesto ")
else:
 print "El a�o "+str(a)+" No es bisiesto " 