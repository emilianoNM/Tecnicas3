class singleton(object):

 def _init_(self, Latitud, Longitud):
  if Latitud>33:
            raise ValueError("Latitud no corresponde a mexico")
  if Longitud<118:
            
            raise ValueError("Longitud no corresponde a mexico")
self.__Latitud=Latitud
   
self.__Longitud=Longitud
      
def getLatitud(self):
    return self.posicion.getLatitud
