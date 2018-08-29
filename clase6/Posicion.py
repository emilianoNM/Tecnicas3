#Posicion.py
class Posicion(object):
	"""docstring for Posicioni"""
	def __init__(self, Latitud,Longitud):
		if Latitud >33:
			raise  ValueError('Latitud no corresponde a la region de mexico') 
		if Longitud < -118:
			raise  ValueError('Longitud no corresponde a la region de mexico') 
		self.__Latitud = Latitud
		self.__Longitud= Longitud
	def getLatitud(self):
		return self.__Latitud
	def getLongitud(self):
		return self.__Longitud
