def nomina(horas,precio):
	if horas<=40:
		nb=horas*precio
	elif horas>40:
		ne=(horas-40)*1.5*precio
		nn=(40*precio)
		nb=ne+nn
	else:
		print 'no valido'
	return nb
op=1
while op==1:
	horas=int(input('cuantas horas trabajo '))
	precio=int(input('cuanto cobra'))
	nom=nomina(horas,precio)
	print nom 
	op=int(input('otro [1]/[0]'))