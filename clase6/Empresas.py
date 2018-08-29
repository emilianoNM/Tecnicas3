from Posicion import Posicion
class UnidadEconomica(object):

    def __init__(self,Nombre,Latitud,Longitud):
            self.Nombre=Nombre
            self.__posicion=Posicion(Latitud,Longitud)
    def getPosicion(self):

    	    return ( self.__posicion)
    def getLatitud(self):
    	   return self.__posicion.getLatitud()
    def getLongitud(self):
    	    return self.__posicion.getLongitud()
    #retornar la distancia de la ubicacion anterior en metros 
    def reUbicacion(self,posicion2):
    	
    	return 12
