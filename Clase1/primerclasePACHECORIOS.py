Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'funciones python'

def __miSegundaFuncion__(argumento2):
     print " segunda  =%s funcion argumento2=%s"%(argumento2 ,123)

def  miPrimerFuncion(argumento1,argumento2):
	print 'hola mundo primer funcion'
	print argumento1
	print argumento2
	__miSegundaFuncion__(argumento1)
	pass 


miPrimerFuncion(10,2)