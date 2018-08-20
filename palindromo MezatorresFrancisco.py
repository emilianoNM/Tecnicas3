
palindromos = [
    
	'anita lava la tina'
]


def es_palindromo(p):
    
	estandar = str(p).lower().replace(' ','')
    
	return estandar == estandar[::-1]
    

if _name_ == '_main_':
   
	for p in palindromos:
        
		resultado = es_palindromo(p)
    
	print(resultado)