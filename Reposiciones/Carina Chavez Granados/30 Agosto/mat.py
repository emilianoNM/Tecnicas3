
def circulo():
	r=input("Ingresa el radio del circulo: ")
	per=2*3.1415*r
	area=3.1415*(r**2)
	return "el perimetro es: "+str(per)+" y el area es: "+str(area)

def esfera():
	r=input("Ingresar radio de la esfera:")
	return "el volumen de la esfera es: ", (4/3)*(3.1415)*(r**3)

def pitagoras():
	cat1=input("Ingresa el primer cateto: ")
	cat2=input("Ingresa el segundo cateto: ")
	hip=((cat1**2)+(cat2**2))**(1/2)
	return "la hipotenusa es: "+str(hip)

print "1... Calcula el perimetro y el area de un circulo"
print "2... Calcula el volumen de una esfera"
print "3... Calcula la hipotenusa de un triangulo"
n=input("Escoje una opcion: ")
if n==1:
	print circulo()
elif n==2:
	print esfera()
elif n==3:
	print pitagoras()
