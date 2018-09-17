#Programa que calcula raices reales de un polinomio de grado dos

def raices():
	x=0
	y=0
	print "Para el polinomio de forma : ax^2 + bx + c"
	a=float(input ("Ingrese el valor para a "))
	b=float(input ("Ingrese el valor para b "))
	c=float(input ("Ingrese el valor para c "))
	y=((b**2)-(4*a*c))
	if y<0:
		return "El polinomio solo tiene raices IMAGINARIAS" 
	else:
		x=((-b)+(((b**2)-(4*a*c))**(1/2)))/(2*a)

		return "Sus raices son: "+str(x)+","+str(-x)
print raices()
