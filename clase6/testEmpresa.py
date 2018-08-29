#testEmpresa.py
import Empresas
from Posicion import Posicion

primerEmpresa=Empresas.UnidadEconomica('Asimov',31,1)

if primerEmpresa.Nombre=="Asimov":
	print "Nombre Empresa correcto"
else:
	raise ValueError('Error en defincion de Nombre') 

if primerEmpresa.getLatitud()==31:
	print "Latitud Empresa correcto"
else:
	raise ValueError('Error en dato de Latitud') 

if primerEmpresa.getLongitud()==1:
	print "Longitud Empresa correcto"
else:
	raise ValueError('Error en dato de Longitud') 

print primerEmpresa.getPosicion()

print primerEmpresa.getLatitud()

#primerEmpresa.posicion.__Latitud=150

print primerEmpresa.getLatitud()


print primerEmpresa.getLatitud()

distancia=primerEmpresa.reUbicacion(Posicion(22,10))

print "distancia entre ubucaciones  ", distancia