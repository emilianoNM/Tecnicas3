a=[1]
a[0]=int(input('Ingresa un numero'))

for i in range (1, a[0]+1):
	a+=[input('Ingresa un numero: ')]

print a

menor=a[0]
for n in a:
	if n<menor:
		menor=n

print menor