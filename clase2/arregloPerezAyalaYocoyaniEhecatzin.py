ancho = 5

for x in list(range(ancho)+list(reversed(range(ancho)))):
	print ' '*(ancho-x-1),'{:#<{w2}}'.format('','',w2=x*2+1)