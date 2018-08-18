def palindromo(c):
	d=c.lower().replace(' ','')
	if d==d[::-1]:
		print 'true'

c = input('Ingrese una frase: ') 
palindromo(c)