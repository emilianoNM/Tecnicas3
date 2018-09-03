
from  EjemploHerencia import Perro 
from  EjemploHerencia import  Gato



firu=Perro("firulais","Grande")

#print dir(firu)
#print type(firu)
print str(Perro)
print firu.MiInformacion()

felix=Gato("felix","Angora")

#print dir(felix)
#print type(felix)

print felix.MiInformacion()


GuarderiaDeAnimales=[Perro("firulais","Grande"),
						Perro("luky","Gigante"),
						Perro("chincharron","chiquito"),
						Perro("zanson","mediano"),
						Gato("felix","Angora"),
						Gato("Garfiel","de la calle"),
						Gato("silvester","siames")]



#print GuarderiaDeAnimales

for animalGuarderia in GuarderiaDeAnimales:
	print animalGuarderia , firu
	print firu==animalGuarderia
	print animalGuarderia==firu