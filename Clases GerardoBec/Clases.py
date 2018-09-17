
# coding: utf-8

# In[ ]:


class Censos(object):
    def __init__(self, estadistica, poblacion, periodo, individuos,encuesta, muestreo, entrevista, error, pais, demografia):
        self.estadistica=estadistica
        self.poblacion=poblacion
        self.periodo=periodo
        self.individuos=individuos
        self.encuesta=encuesta
        self.muestreo=muestreo
        self.entrevista=entrevista
        self.error=error
        self.pais=pais
        self.demografia=demografia

class Gobierno(object):
    def __init__(self, estado, autoridad, instituciones, politica, poderejecutivo, poderlegislativo, poderjudicial, constitucion, sociedad, gabinete):
        self.estado=estado
        self.autoridad=autoridad
        self.instituciones=instituciones
        self.politica=politica
        self.poderejecutivo=poderejecutivo
        self.poderlegislativo=poderlegislativo
        self.poderjudicial=poderjudicial
        self.constitucion=constitucion
        self.sociedad=sociedad
        self.gabinete=gabinete
        
class Poblacion(object):
    def __init__(self, area, espaciogeografico, pueblo, demografia, sociologia, economia, muerte, emigracion, cultura, religion):
        self.area=area
        self.espaciogeografico=espaciogeografico
        self.pueblo=pueblo
        self.demografia=demografia
        self.sociologia=sociologia
        self.economia=economia
        self.muerte=muerte
        self.emigracion=emigracion
        self.cultura=cultura
        self.religion=religion
        
class Ocupacion(object):
    def __init__(self, doctor, maestro, ingeniero, arquitecto, abogado, contador, agricultor, psicologo, biologo, actor):
        self.doctor=doctor
        self.maestro=maestro
        self.ingeniero=ingeniero
        self.arquitecto=arquitecto
        self.abogado=abogado
        self.contador=contador
        self.agricultor=agricultor
        self.psicologo=psicologo
        self.biologo=biologo
        self.actor=actor
        
class Empleo(object):
    def __init__(self, trabajo, contrato, colectivo, salario, empleado, empleador, desempleo, ingreso, egreso, edad):
        self.trabajo=trabajo
        self.contrato=contrato
        self.colectivo=colectivo
        self.salario=salario
        self.empleado=empleado
        self.empleador=empleador
        self.desempleo=desempleo
        self.ingreso=ingreso
        self.egreso=egreso
        self.edad=edad
        
class Seguridad(object):
    def __init__(self, riesgo, confianza, bienestar, ambiente, nivel, ley, conductasocial, criminalistica, delito, medidas):
        self.riesgo=riesgo
        self.confianza=confianza
        self.bienestar=bienestar
        self.ambiente=ambiente
        self.nivel=nivel
        self.ley=ley
        self.conductasocial=conductasocial
        self.criminalistica=criminalistica
        self.delito=delito
        self.medidas=medidas

class Tecnologia(object):
    def __init__(self, ciencia, diseño, servicios, adaptacion, necesidades, tecnica, recursos, educacion, comercializacion, producto):
        self.ciencia=ciencia
        self.diseño=diseño
        self.servicios=servicios
        self.adaptacion=adaptacion
        self.necesidades=necesidades
        self.tecnica=tecnica
        self.recursos=recursos
        self.educacion=educacion
        self.comercializacion=comercializacion
        self.producto=producto
        
class ActividadEconomica(object):
    def __init__(self, productos, bienes, servicios, necesidades, poblacion, ciudad, region, pais, distribucion, recursos):
        self.productos=productos
        self.bienes=bienes
        self.servicios=servicios
        self.necesidades=necesidades
        self.poblacion=poblacion
        self.ciudad=ciudad
        self.region=region
        self.pais=pais
        self.distribucion=distribucion
        self.recursos=recursos
        
class Sectores(object):
    def _init_(self, primario, secundario, terciario, cuaternario, nadiario, economico, region, industria, sociedad, informacion):
        self.primario=primario
        self.secundario=secundario
        self.terciario=terciario
        self.cuaternario=cuaternario
        self.nadiario=nadiario
        self.economico=economico
        self.region=region
        self.industria=industria
        self.sociedad=sociedad
        self.informacion=informacion

class Areageografica(object):
    def _init_(self, aguascalientes, bajacalifornia, bajacaliforniasur, campeche, chiapas, coahuila, colima, ciudaddemexico, durango, estadodemexico):
        self.aguascalientes=aguascalientes
        self.bajacalifornia=bajacalifornia
        self.bajacaliforniasur=bajacaliforniasur
        self.campeche=campeche
        self.chiapas=chiapas
        self.coahuila=coahuila
        self.colima=colima
        self.ciudaddemexico=ciudaddemexico
        self.durango=durango
        self.estadodemexico=estadodemexico
            
class Agropecuario(object):
    def _init_(self, primario, agricola, ganadero, economia, caza, pesca, industria, rural, produccion, valor):
        self.primario=primario
        self.agricola=agricola
        self.ganadero=ganadero
        self.economia=economia
        self.caza=caza
        self.pesca=pesca
        self.industria=industria
        self.rural=rural
        self.produccion=produccion
        self.valor=valor
        
class Entornourbano(object):
    def _init_(self, zona, medio, area, centro, territorio, geografia, paisaje, ciudad, servicios, factores):
        self.zona=zona
        self.medio=medio
        self.area=area
        self.centro=centro
        self.territorio=territorio
        self.geografia=geografia
        self.paisaje=paisaje
        self.ciudad=ciudad
        self.servicios=servicios
        self.factores=factores
            
class Establecimiento(object):
    def _init_(self, espacio, bienes, economia, servicios, mercancia, venta, comercio, produccion, consumidor, distribucion):
        self.espacio=espacio
        self.bienes=bienes
        self.economia=economia
        self.servicios=servicios
        self.mercancia=mercancia
        self.venta=venta
        self.comercio=comercio
        self.produccion=produccion
        self.consumidor=consumidor
        self.distribucion=distribucion
        
class Urbanizacion(object):
    def _init_(self, viviendas, rural, poblacion, zonas, construccion, terreno, pais, ciudad, tasa, comercio):
        self.viviendas=viviendas
        self.rural=rural
        self.poblacion=poblacion
        self.zonas=zonas
        self.construccion=construccion
        self.terreno=terreno
        self.pais=pais
        self.ciudad=ciudad
        self.tasa=tasa
        self.comercio=comercio
        
class Salud(object):
    def _init_(self, bienestar, fisico, mental, social, equilibrio, estado, enfermedad, medicina, oms, ejercicio):
        self.bienestar=bienestar
        self.fisico=fisico
        self.mental=mental
        self.social=social
        self.equilibrio=equilibrio
        self.estado=estado
        self.enfermedad=enfermedad
        self.medicina=medicina
        self.oms=oms
        self.ejercicio=ejercicio
        
class Calidaddevida(object):
    def _init_(self, condiciones, economicas, sociales, politicas, salud, naturales, bienestar, desarrollo, educacion, idh):
        self.condiciones=condiciones
        self.economicas=economicas
        self.sociales=sociales
        self.politicas=politicas
        self.salud=salud
        self.naturales=naturales
        self.bienestar=bienestar
        self.desarrollo=desarrollo
        self.educacion=educacion
        self.idh=idh
        
class Productividad(object):
    def _init_(self, sistema, produccion, recursos, tiempo, resultados, eficiencias, calidad, empresas, trabajo, tecnologia):
        self.sistema=sistema
        self.produccion=produccion
        self.recursos=recursos
        self.tiempo=tiempo
        self.resultados=resultados
        self.eficiencias=eficiencias
        self.calidad=calidad
        self.empresas=empresas
        self.trabajo=trabajo
        self.tecnologia=tecnologia
        
class Innovacion(object):
    def _init_(self, cambio, novedad, renovar, crear, propuesta, invento, difusion, empremdedor, ciencia, creatividad):
        self.cambio=cambio
        self.novedad=novedad
        self.renovar=renovar
        self.crear=crear
        self.propuesta=propuesta
        self.invento=invento
        self.difusion=difusion
        self.empremdedor=empremdedor
        self.ciencia=ciencia
        self.creatividad=creatividad
        
class Manufactura(object):
    def _init_(self, fabricacion, produccion, bienes, industria, materiaprima, distribucion, consumo, diseño, mercado, sociedad):
        self.fabricacion=fabricacion
        self.produccion=produccion
        self.bienes=bienes
        self.industria=industria
        self.materiaprima=materiaprima
        self.distribucion=distribucion
        self.consumo=consumo
        self.diseño=diseño
        self.mercado=mercado
        self.sociedad=sociedad
        
class Ubicacion(object):
    def _init_(self, geografia, coordenadas, superficie, latitud, longitud, escalas, geolocalizacion, mapa, infraestructura, orientacion): 
        self.geografia=geografia
        self.coordenadas=coordenadas
        self.superficie=superficie
        self.latitud=latitud
        self.longitud=longitud
        self.escalas=escalas
        self.geolocalizacion=geolocalizacion
        self.mapa=mapa
        self.infraestructura=infraestructura
        self.orientacion=orientacion

