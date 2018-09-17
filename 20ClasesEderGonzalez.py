
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


#20 Clases Empresa
#Por Cblue (Ricardo V.T)


# In[ ]:


class NombreEmpresa:
    def__init__(self,nombre,siglasEMpresa,antiguedad):
        self.nombre=nombre
        self.siglasEmpresa=siglasEmpresa
        self.antiguedad=antiguedad

        
        
class DireccionEmpresa(object):
    def__init__(self,ciudad,delegacion,municipio,CP,calle,numero,coordenadas):
        self.ciudad=ciudad
        self.delegacion=delegacion
        self.municipio=municipio
        self.CP=CP
        self.calle=calle
        self.numero=numero
        self.coordenadas=coordenadas
        

class RazonSocial(object):
    def__init__(self,SA,SAC,SRL,EIRL,SAA,NoDefinida):
        self.SA=SA
        self.SAC=SAC
        self.SRL=SRL
        self.EIRL=EIRL
        self.SAA=SAA
        self.NoDefiida=NoDefinida
        

class Atencion(object):
    def__init__(self, horarioDeAtencion,HDATelefonica,HDAVecntanillas):
        self.horarioDeAtencion=horarioDeAtencion
        self.HDATelefonica=HDATelefonica
        self.HDAVentanilla=HDAVentanilla
        
        
class Prestaciones(object):
    def__init__(self, servicios, productos, actividades, proyectos ):
        self.servicios=servicios
        self.productos=productos
        self.actividades=actividades
        self.proyectos=proyectos
        
        
class relevancia(object):
    def__init__(self, CaracterInternacional,CaracterNacional,Prestigio,Asociaciones, Deals, Dealers ):
        self.CaracterInternacional=CaracterInternacional
        self.CaracterNacional=CaracterNacional
        self.Prestigio=Prestigio
        self.Asociaciones=Asociaciones
        self.Deals=Deals
        self.Dealers=Dealers
        

class Contacto(obejct):
    def__init__(self,LineaTel,CorreoE,RedesSociales,WebPage,AplicacionMovil):
        self.Lineatel=LineaTel
        self.CorreoE=CorreoE
        self.RedesSociales=RedesSociales
        self.WebPage=WebPage
        self.AplicacionMovil=AplicacionMovil
        
        
class OfertaLaboral(object):
    def__init__(self,Puestos,DisponibilidadVacantes,Requisitos,HRSLaborales,CondicionesLab):
        self.Puestos=Puestos
        self.DisponibilidadVacantes=DisponibilidadVacantes
        self.Requisitos=Requisitos
        self.HRSLaborales=HRSLaborales
        self.CondicionesLab
        

class Empleado(object):
    def__init__(self,NombreEmp,sexo,Puesto,Salario,Antiguedad,NumTrabajador,Horario,Experiencia):
        self.NombreEmp=NombreEmp
        self.sexo=sexo
        self.Puesto=Puesto
        self.Salario=Salario
        self.Antiguedad=Antiguedad
        self.NumTrabajador=NumTrabajador
        self.Horario=Horario
        self.Experiencia=Experiencia
        
    
class opiniones(object):
    def__init__(self,buenasop,malasop,regularesop,excelentesop, reseñasEmp, reseñasConsumidores, reseñasSocios):
        self.buenasop=buenasop
        self.malasop=malasop
        self.regularesop=regularesop
        self.excelentesop=excelentesop
        self.reseñasEmp=reseñasEmp
        self.reseñasConsumidores=reseñasConsumidores
        self.reseñasSocios=reseñasSocios
        

class organizacion(object):
    def__init__(self,direccion, jerarquias, comites, sindicatos):
        self.direccion=direccion
        self.jerarquias=jerarquias,
        self.comites=comites
        self.sindicatos=sindicatos
        
        
class Administracion(object):
    def__init(self,contabilidad,gestion,asesoria,defensoria,controlCalidad, planificacion, evaluacion):
        self.contabilidad=contabilidad
        self.gestion=gestion
        self.asesoria=asesoria
        self.defensoria=defensoria
        self.controlCalidad=controlCalidad}
        self.planificacion=planificacion
        self.evaluacion=evaluacion


class promocion(object):
    def__init__(anunciospublicitarios, difamacionServ, presentaciones, conferencias):
        self.anunciospublicitarios=anunciospublicitarios
        self.difamacionServ=difamacionServ
        self.presentaciones=presentaciones
        self.conferencias=conferencias
        
        
class Identificador(object):
    def__init__(self,LogotipoEMP,ColorCaracteristico)
        self.LogotipoEMP=LogotipoEMP
        self.ColorCaracteristico=ColorCaracteristico
        
        
class Documentacion(object):
    def__init__(self,ActaCons,Declaraciones,Deudas, XComisiones, CondicionesL):
        self.ActaCons=ActaCons
        self.Declaraciones=Declaraciones
        self.Deudas=Deudas
        self.XComisiones=XComisiones
        self.CondicionesL=CondicionesL

