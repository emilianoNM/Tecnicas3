###pasar de celcius a fahrenheit y viceversa

n=int(input("Seleccione Conversion\n1. �C a �F\n2. �F a �C\n" ))
if(n==1):
 c=float(input("Ingrese grados Celsius\n"))
 f=c*(9/5)+32
 print(str(c)+"�C equivale a "+str(f)+"�F")
else:
 f=float(input("Ingrese grados Fahrenheit\n"))
 c=(f-32)*(5/9)
 print(str(f)+"�F equivale a "+str(c)+"�C")