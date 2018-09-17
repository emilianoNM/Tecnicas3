#Este programa calcula area y perimetro de rectangulo mediante la base y altura o coordenadas
#Chavez Granados

def rectangulo():
	b=input("escribe la base del rectangulo: ")
	h=input("ingresa su altura: ")
	per=(2*b)+(2*h)
	area=b*h
	return "el perimetro es: "+str(per)+" y el area es: "+str(area)

def coord():
	x1=input("Ingresa la coordenada x1")
	x2=input("Ingresa la coordenada x2")
	y1=input("Ingresa la coordenada y1")
	y2=input("Ingresa la coordenada y2")
	areac= (x2-x1)*(y2-y1)
	peri= 2*(x2-x1)+2*(y2-y1)
	return "el perimetro es: "+str(peri)+" y el area es: "+str(areac)

print "*Calculo de Area y Perimetro de un Rectangulo:*"
print "(1) Calcula el perimetro y el area de un RECTANGULO"
print "(2) Calcula el area de un RECTANGULO desde sus Coordenadas"
var=input("Escoje tu opcion: ")
if var==1:
	print rectangulo()
elif var==2:
	print coord()

else:
	print "Ingrese un numero entre las opciones"
