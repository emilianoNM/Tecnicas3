#funciones python 
print 'funciones python'

def __miSegundaFuncion__(argumento2):
     print " segunda  =%s funcion argumento2=%s"%(argumento2 ,123)

def  miPrimerFuncion(argumento1,argumento2):
	print 'hola mundo primer funcion'
	print argumento1
	print argumento2
	__miSegundaFuncion__(argumento1)
	pass 


miPrimerFuncion(10,2)
