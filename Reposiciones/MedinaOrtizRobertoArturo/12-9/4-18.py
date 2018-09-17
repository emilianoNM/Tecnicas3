a=[]
for i in range (0,5):
	a+=[input('Ingresa un numero: ')]
a=map(int,a)
for i in range (0,5):
	print '*'*a[i]