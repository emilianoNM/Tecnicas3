Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> class  Empresa:
    print("Pacheco Rios Jesus C.")
	def __init__(self,nombre):
		self.__nombre=nombre
		print self.__nombre
	def  getNombre(self):
		if self.__nombre == 'Asimov' :
			return "Es la mejor empresa del mundo "+self.__nombre
		else :
			 return self.__nombre

variableEmpresaAsimov=Empresa("Asimov")

print variableEmpresaAsimov
print dir(variableEmpresaAsimov)
print type(variableEmpresaAsimov)
print variableEmpresaAsimov.getNombre()


variableEmpresa=Empresa("MAIA")

print variableEmpresa
print dir(variableEmpresa)
print type(variableEmpresa)
print variableEmpresa.getNombre()

print variableEmpresaAsimov.getNombre()