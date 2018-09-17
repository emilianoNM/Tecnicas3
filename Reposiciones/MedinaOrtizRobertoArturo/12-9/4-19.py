def ventas (prod,cant):
	venta=0
	if prod==1:
		venta=2.98*cant
	elif prod==2:
		venta=4.5*cant
	elif prod==3:
		venta=9.98*cant
	elif prod==4:
		venta=4.49*cant
	elif prod==5:
		venta=6.87*cant
	else:
		print 'Producto no existe'

	return venta

op=1
v=0
while op==1:
	prod=int(input('Ingrese el procudcto'))
	cant=int(input('Ingrse la cantidad vendida' ))
	v=v+ventas(prod,cant)
	print 'producto ',prod,' vendido ',v
	op=input('Agregar mas [1]/[0]')
	print op
	

print 'Ventas totales: ',v

