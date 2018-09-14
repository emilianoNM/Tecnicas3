#Instalaciones de la Empresa

class Instalaciones(object):
	"""docstring for Instalaciones"""
	def __init__(self, Sucursales, Edificios, CentrosdeDistribucion, Almacenes, CentrosdeProduccion
						Laboratorios, CentrosdeInvestigacion, Sedes, Locales):
		
		self.Sucursales=Sucursales
		self.Edificios=Edificios
		self.CentrosdeDistribucion=CentrosdeDistribucion
		self.CentrosdeInvestigacion=CentrosdeInvestigacion
		self.CentrosdeProduccion=CentrosdeProduccion
		self.Almacenes=Almacenes
		self.Laboratorios=Laboratorios
		self.Sedes=Sedes
		self.Locales=Locales
