###pasar de celcius a fahrenheit y viceversa

n=int(input("Seleccione Conversion\n1. ºC a ºF\n2. ºF a ºC\n" ))
if(n==1):
 c=float(input("Ingrese grados Celsius\n"))
 f=c*(9/5)+32
 print(str(c)+"ºC equivale a "+str(f)+"ºF")
else:
 f=float(input("Ingrese grados Fahrenheit\n"))
 c=(f-32)*(5/9)
 print(str(f)+"ºF equivale a "+str(c)+"ºC")