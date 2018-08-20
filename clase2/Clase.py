#clase 1 

class  Empresa:
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