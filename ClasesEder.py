
# coding: utf-8

# In[ ]:


class Empleados(object):
	
	def __init__(self, numerodeempleados, nodeempleado, experiencia, salario,posicion,antiguedad,nombre,sexo,idiomashablados,anodeingreso):
		
        self.nodeempleado=nodeempleado
		self.numerodeempleados=numerodeempleados
		self.posicion=posicion
		self.experiencia=experiencia
		self.salario=salario
		self.antiguedad=antiguedad
		self.nombre=nombre
		self.sexo=sexo
		self.idiomashablados=idiomashablados
		self.anodeingreso=anodeingreso
class  Ubicacion(object):
	
	def __init__(self, latitud,altitud,coordenadas,cp, ciudad,delegacion,tipozona,calle,numero,estado):
		
		self.latitud=latitud
		self.altitud=altitud
        self.coordenadas=coordenadas
		self.cp=cp
		self.ciudad=ciudad
		self.delegacion=delegacion
		self.tipozona=tipozona
		self.calle=calle
		self.numero=numero
		self.estado=estado
class Razonsocial(object):
    def __init__(self, ind, sa, sr, scc,sc, eu, sac):
		self.ind=ind
		self.sa=sa
		self.sr=sr
		self.scc=scc
		self.sc=sc
		self.eu=eu
		self.sac=sac
class Actividadeconomica(object):
    def __init__(self, actividad,tipo, servicios, productos):
		self.actividad=actividad
		self.tipo=tipo
		self.servicios=servicios
		self.productos=productos
class RedesSociales():
    
    def __init__(self, facebook, twitter,snapchat, instagram, paginaweb, linkeldin, correo, youtube, usuarios, seguidores):
        
        self.facebook = facebook
        self.twiter = twiter
        self.snapchat=snapchat
        self.instagram = instagram
        self.paginaweb = paginaweb
        self.linkeldin = linkeldin
        self.correo = correo
        self.youtube = youtube
        self.usuarios = usuarios
        self.seguidores = seguidores
        self.imagenesDeReconocimiento = imagenesDeReocnocimiento
class Informacion():
    
    def __init__(self,nacional,internacional,multinacional, trabajadores, asociaciones, sindicatos, empleo, valoracion, proyectos, calificacion):
        
        self.nacional=nacional
        self.internacional=internacional
        self.asociaciones = asociaciones
        self.sindicatos = sindicatos
        self.empleo = empleo
        self.valoracion = valoracion
        self.proyectos = proyectos
        self.multinacional=multinacional
        self.trabajadores = trabajadores
        self.calificacion = calificacion

class movimientos(object):
    def __init__(self,numventas,inversionistas,transacciones,capital, trabajadores, sucursales,ganancias,perdidas,impuestos,sueldo):
        self.numventas=numventas
        self.capital=capital
        self.trabajadores=trabajadores
        self.ganancias=ganancias
        self.perdidas=perdidas
        self.impuestos=impuestos
        self.sucursales=sucursales
        self.transacciones=transacciones
        self.sueldo=sueldo
class Relaciones(object):
    def __init__(self, distribuidores,tiempoexpansion,patentes,clientes, competencias,sucursales, tiempoexpansion,CamaraConsesionario, inversionistas,socios):
        self.tiempoexpansion=tiempoexpansion
        self.distribuidores=distribuidores
        self.inversionistas=inversionistas
        self.clientes=clientes
        self.competencias=competencias
        self.socios=socios
        self.sucursales=sucursales
        self.CamaraConsesionario=CamaraConsesionario
        self.patentes=patentes
class confianza(object):
    def _init_(self,certificaciones,seguro,hacienda,licitaciones,legislaciones,foda,registro,identificacion,valor,evaluacion)
    self.certificaciones=certificaciones
    self.seguro=seguro
    self.hacienda=hacienda
    self.licitaciones=licitaciones
    self.legislaciones=legislaciones
    self.foda=foda
    self.registro=registro
    self.identificacion=identificacion
    self.valor=valor
    self.evaluacion=evaluacion


class Agricultura(object):
    def _init_(aclasedeactividad, anombre,arazonsocial, acorreoe, apaginadeinternet, atipodeestablecimiento,atelefono,aide, acd, anumempleados):
            self.aclasedeactividad=aclasedeactividad
            self.anombre=anombre
            self.arazonsocial=arazonsocial
            self.acorreoe=acorreoe
            self.apaginadeinternet=apaginadeinternet
            self.atipodeestablecimiento=atipodeestablecimiento
            self.atelefono=atelefono
            self.aide=aide
            self.acd=acd
            self.anumempleados=anumempleados
class deporteycultura(object):
         def _init_(dcnombre,dcide,dcactividades,dcpeventos,dctelefono,dcciudad,dcnumempleados,dcactividad,dcasociaciones,dcvoluntarios,dcfechaincorporacion):
        self.dcnombre=dcnombre
        self.dcide=dcide
        self.dcactividades=dcactividades
        self.dceventos=dceventos
        self.dctelefono=dctelefono
        self.dcciudad=dcciudad
        self.dcnumempleados=dcnumempleados
        self.dcactividad=dcactividad
        self.dcasociones=dcasociaciones
        self.dcvoluntarios=dcvoluntarioz
        self.dcfechaincorporacion=dcfechaincorporacion
        
            
class Mineria(object):
    def _init_(mnombre,mide,mcorreoe,mmetales,mtelefono,mzona,mnumempleados,mactividad,mtipounidadeconomica,mfechaincorporacion):
        self.mnombre=mnombre
        self.mide=mide
        self.mcorreoe=mcorreoe
        self.mmetales=mmetales
        self.mtelefono=mtelefono
        self.mzona=mzona
        self.mnumempleados=mnumempleados
        self.mactividad=mactividad
        self.mtipounidadeconomica=mtipounidadeconomica
        self.mfechaincorporacion=mfechaincorporacion
        

class construccion(object):
       def _init_(cnombre,cide,ccorreoe,cpaginainternet,ctelefono,cciudad,cnumempleados,cactividad,ctipounidadeconomica,cfechaincorporacion):
        self.cnombre=cnombre
        self.cide=cide
        self.ccorreoe=ccorreoe
        self.cpaginadeinternet=cpaginadeinternet
        self.ctelefono=ctelefono
        self.cciudad=cciudad
        self.cnumempleados=cnumempleados
        self.cactividad=cactividad
        self.ctipounidadeconomica=ctipounidadeconomica
        self.cfechaincorporacion=cfechaincorporacion
        
class serviciostecnologicosytecnicos(object):
        def _init_(stnombre,stide,stcorreoe,stpaginainternet,sttelefono,stciudad,stnumempleados,stactividad,sttipounidadeconomica,stfechaincorporacion):
        self.stnombre=stnombre
        self.stide=stide
        self.stcorreoe=stcorreoe
        self.stpaginadeinternet=stpaginadeinternet
        self.sttelefono=sttelefono
        self.stciudad=stciudad
        self.stnumempleados=stnumempleados
        self.stactividad=stactividad
        self.sttipounidadeconomica=sttipounidadeconomica
        self.stfechaincorporacion=stfechaincorporacion
        
class corporativos(object):
        def _init_(conombre,coide,cocorreoe,copaginainternet,cotelefono,cociudad,conumempleados,coactividad,cotipounidadeconomica,cofechaincorporacion):
        self.conombre=conombre
        self.coide=coide
        self.cocorreoe=cocorreoe
        self.copaginadeinternet=copaginadeinternet
        self.cotelefono=cotelefono
        self.cociudad=cociudad
        self.conumempleados=conumempleados
        self.coactividad=coactividad
        self.cotipounidadeconomica=cotipounidadeconomica
        self.cofechaincorporacion=cofechaincorporacion
        
        
class serviciosdesalud(object):
        def _init_(ssnombre,sside,sstipo,sspaginainternet,sscertificaciones,anoexperiencia,sstelefono,ssciudad,ssnumempleados,ssactividad,sstipounidadeconomica,ssfechaincorporacion):
        self.ssnombre=ssnombre
        self.sside=sside
        self.sstipo=sstipo
        self.sscertificaciones=sscertificaciones
        self.anoexperiencia=anoexperiencia
        self.sspaginadeinternet=sspaginadeinternet
        self.sstelefono=sstelefono
        self.ssciudad=ssciudad
        self.ssnumempleados=ssnumempleados
        self.ssactividad=ssactividad
        self.sstipounidadeconomica=sstipounidadeconomica
        self.sstipounidadeconomica=sstipounidadeconomica
        

class transporte(object):
        def _init_(ttnombre,ttide,ttamano,ttipo,ttzona,ttpaginainternet,tttelefono,ttciudad,ttnumempleados,ttactividad,tttipounidadeconomica,ttfechaincorporacion):
        self.ttnombre=ttnombre
        self.ttide=ttide
        self.ttamano=ttamano
        self.ttipo=ttipo
        self.ttzona=ttzona
        self.ttpaginadeinternet=ttpaginadeinternet
        self.tttelefono=tttelefono
        self.ttciudad=ttciudad
        self.ttnumempleados=ttnumempleados
        self.ttactividad=ttactividad
        self.tttipounidadeconomica=tttipounidadeconomica
        self.ttfechaincorporacion=ttfechaincorporacion
class educacion(object):
        def _init_(enombre,eide,ecorreoe,epaginainternet,etelefono,eciudad,enumempleados,eactividad, etipounidadeconomica,efechaincorporacion):
        self.enombre=enombre
        self.eide=eide
        self.ecorreoe=ecorreoe
        self.epaginadeinternet=epaginadeinternet
        self.etelefono=etelefono
        self.eciudad=eciudad
        self.enumempleados=enumempleados
        self.eactividad=eactividad
        self.etipounidadeconomica=etipounidadeconomica
        self.efechaincorporacion=efechaincorporacion
class inmobiliario(object):
        def _init_(inombre,iide,icorreoe,ipaginainternet,itelefono,iciudad,inumempleados,iactividad,itipounidadeconomica,ifechaincorporacion):
        self.inombre=inombre
        self.iide=iide
        self.icorreoe=icorreoe
        self.ipaginadeinternet=ipaginadeinternet
        self.itelefono=itelefono
        self.iciudad=iciudad
        self.inumempleados=inumempleados
        self.iactividad=iactividad
        self.itipounidadeconomica=itipounidadeconomica
        self.ifechaincorporacion=ifechaincorporacion
class generaciontransmicion(object):
        def _init_(gnombre,gide,gcorreoe,gpaginainternet,gtelefono,gciudad,gnumempleados,gactividad,gtipounidadeconomica,gfechaincorporacion): 
        self.gnombre=gnombre
        self.gide=gide
        self.gcorreoe=gcorreoe
        self.gpaginadeinternet=gpaginadeinternet
        self.gtelefono=gtelefono
        self.gciudad=gciudad
        self.gnumempleados=gnumempleados
        self.gactividad=gactividad
        self.gtipounidadeconomica=gtipounidadeconomica
        self.gfechaincorporacion=gfechaincorporacion

class industriasmanufactureras(object):
        def _init_(imnombre,imide,proovedores,immateriales,imindustrias,imtipo,imciudad,imnumempleados,imactividad,imtipounidadeconomica,imfechaincorporacion): 
        self.imnombre=imnombre
        self.imide=imide
        self.improovedores=improovedores
        self.immateriales=immateriales
        self.imindustrias=imindustrias
        self.imciudad=imciudad
        self.imtipo=imtipo
        self.imnumempleados=imnumempleados
        self.imactividad=imactividad
        self.imtipounidadeconomica=imtipounidadeconomica
        self.imfechaincorporacion=imfechaincorporacion

class comerciopormayor(object):
        def _init_(cpmnombre,cpmide,cpmorreoe,cpmpaginainternet,cpmtelefono,cpmciudad,cpmnumempleados,cpmactividad,cpmtipounidadeconomica,cpmfechaincorporacion): 
        self.cpmnombre=cpmnombre
        self.cpmide=cpmide
        self.cpmcorreoe=cpmcorreoe
        self.cpmpaginadeinternet=cpmpaginadeinternet
        self.cpmtelefono=cpmtelefono
        self.cpmciudad=cpmciudad
        self.cpmnumempleados=cpmnumempleados
        self.cpmactividad=cpmactividad
        self.cpmtipounidadeconomica=cpmtipounidadeconomica
        self.cpmfechaincorporacion=cpmfechaincorporacion

class comerciopormenor(object):
        def _init_(cmnombre,gide,cmcorreoe,cmpaginainternet,cmtelefono,cmciudad,cmnumempleados,cmactividad,cmtipounidadeconomica,cmfechaincorporacion): 
        self.cmnombre=cmnombre
        self.cmide=cmide
        self.cmcorreoe=cmcorreoe
        self.cmpaginadeinternet=cmpaginadeinternet
        self.cmtelefono=cmtelefono
        self.cmciudad=cmciudad
        self.cmnumempleados=cmnumempleados
        self.cmactividad=cmactividad
        self.cmtipounidadeconomica=cmtipounidadeconomica
        self.cmfechaincorporacion=cmfechaincorporacion

class informacionmemasivos(object):
        def _init_(imsnombre,imside,imscorreoe,imspaginainternet,imstelefono,imsciudad,imsnumempleados,imsactividad,imstipounidadeconomica,imsfechaincorporacion): 
        self.imsnombre=imsnombre
        self.imside=imside
        self.imscorreoe=imscorreoe
        self.imspaginadeinternet=imspaginadeinternet
        self.imstelefono=imstelefono
        self.imsciudad=imsciudad
        self.imsnumempleados=imsnumempleados
        self.imsactividad=imsactividad
        self.imstipounidadeconomica=imstipounidadeconomica
        self.imsfechaincorporacion=imsfechaincorporacion

class serviciosfinancieros(object):
    def _init_(sfnombre,sfide,sfcorreoe,sfpaginainternet,sftelefono,sfciudad,sfnumempleados,sfactividad,sftipounidadeconomica,sffechaincorporacion): 
        self.sfnombre=sfnombre
        self.sfide=sfide
        self.sfcorreoe=sfcorreoe
        self.sfpaginadeinternet=sfpaginadeinternet
        self.sftelefono=sftelefono
        self.sfciudad=sfciudad
        self.sfnumempleados=sfnumempleados
        self.sfactividad=sfactividad
        self.sftipounidadeconomica=sftipounidadeconomica
        self.sffechaincorporacion=sffechaincorporacion

class servicioapoyoa(object):
    def _init_(gnombre,gide,gcorreoe,gpaginainternet,gtelefono,gciudad,gnumempleados,gactividad,gtipounidadeconomica,gfechaincorporacion): 
        self.gnombre=gnombre
        self.gide=gide
        self.gcorreoe=gcorreoe
        self.gpaginadeinternet=gpaginadeinternet
        self.gtelefono=gtelefono
        self.gciudad=gciudad
        self.gnumempleados=gnumempleados
        self.gactividad=gactividad
        self.gtipounidadeconomica=gtipounidadeconomica
        self.gfechaincorporacion=gfechaincorporacion

class serviciosalojamientotem(object):
    def _init_(gnombre,gide,gcorreoe,gpaginainternet,gtelefono,gciudad,gnumempleados,gactividad,gtipounidadeconomica,gfechaincorporacion): 
        self.gnombre=gnombre
        self.gide=gide
        self.gcorreoe=gcorreoe
        self.gpaginadeinternet=gpaginadeinternet
        self.gtelefono=gtelefono
        self.gciudad=gciudad
        self.gnumempleados=gnumempleados
        self.gactividad=gactividad
        self.gtipounidadeconomica=gtipounidadeconomica
        self.gfechaincorporacion=gfechaincorporacion

class otrosservicios(object):
    def _init_(osnombre,oside,oscorreoe,ospaginainternet,ostelefono,osciudad,osnumempleados,osactividad,ostipounidadeconomica,osfechaincorporacion): 
        self.osnombre=osnombre
        self.oside=oside
        self.oscorreoe=oscorreoe
        self.ospaginadeinternet=ospaginadeinternet
        self.ostelefono=ostelefono
        self.osciudad=osciudad
        self.osnumempleados=osnumempleados
        self.osactividad=osactividad
        self.ostipounidadeconomica=ostipounidadeconomica
        self.osfechaincorporacion=osfechaincorporacion

class actividadeslegislativas(object):
    def _init_(alnombre,alide,alcorreoe,alpaginainternet,altelefono,alciudad,alnumempleados,alactividad,altipounidadeconomica,alfechaincorporacion): 
        self.alnombre=alnombre
        self.alide=alide
        self.alcorreoe=alcorreoe
        self.alpaginadeinternet=alpaginadeinternet
        self.altelefono=altelefono
        self.alciudad=alciudad
        self.alnumempleados=alnumempleados
        self.alactividad=alactividad
        self.altipounidadeconomica=altipounidadeconomica
        self.alfechaincorporacion=alfechaincorporacion

