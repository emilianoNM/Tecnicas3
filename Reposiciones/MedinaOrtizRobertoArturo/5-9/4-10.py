a=[0]
i=0
s=0
while a[i] !=9999:
	a+=[int(input('Ingrese numero '))]
	i+=1
	s=s+a[i]
	
p=(s-9999)/(i-1)
print 'Promedio: ',p
	
