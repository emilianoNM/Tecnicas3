###tablas de multiplicar

x=int(raw_input("ingrese numero: "))
for i in range(1,x+1):
	for j in range(1,11):
		print "{:>5}".format(i*j),
	print