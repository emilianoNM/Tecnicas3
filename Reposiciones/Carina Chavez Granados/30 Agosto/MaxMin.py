#El programa calcula el maximo o minimo de un polinomio cuadratico

def maxmin():
	x=0.0
	y=0.0
	print "Tenemos un polinomio ax^2 + bx + c"
	a= float(input ("Ingrese el valor para a "))
	b=float(input ("Ingrese el valor para b "))
	c=float(input ("Ingrese el valor para c "))
	x=((-b)/(2*a))
	y=(a*(x**2))+(b*x)+c
	if y>0:
		return "Solo tienen un maximo: "+str(x)+" Con coordenadas ("+str(x)+","+str(y)+")"
	else:
		return "Solo tienen un minimo: "+str(x)+" Con coordenadas ("+str(x)+","+str(y)+")"
print maxmin()
