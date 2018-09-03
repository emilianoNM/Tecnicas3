#Herencia

class Animal(object):
	"""docstring for Animal"""
	def __init__(self, nombre='Sin nombre'):
		self.nombre =nombre

	def MiInformacion(self):
	 	print  ("su nombre "+self.nombre)
	def __str__(self):
		return "Animal"
	def __repr__(self):
		return "Animal"

class  Perro(Animal):

	def __init__(self,nombre,tamano):
		super(Perro,self).__init__(nombre)
		self.tamano=tamano
	def __repr__(self):
		return "Es un Perro de nombre = %s y tamano= %s "%(self.nombre,self.tamano)
	def __eq__(self,other):
		 print "eq"
		 return self.nombre==other.nombre and self.tamano == other.tamano
	def __str__(self):
		return self.nombre



	 	 
class Gato(Animal):
			"""docstring for Gato"""
			def __init__(self,nombre,raza):
				super(Gato, self).__init__(nombre)
				self.raza = raza
			def __repr__(self):
				return "Es un gato nombre= %s de raza %s"%(self.nombre,self.raza)
						
