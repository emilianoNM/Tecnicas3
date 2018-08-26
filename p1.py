print 'Linares Alonso Joshua A.'
#el programa calcula la edad y el a;o de egreso de un alumno o exalumno de la facultad de ingenieria 
class Estudiante:
    edad=0
    ingreso=0
    edad_egreso=0
    def __init__(self):
           self.universidad="UNAM"
           self.semestre="2019-1"
           self.facultad="Facultad de ingenieria"



    def imprimir(self):
          print estunam.universidad
          print estunam.semestre
          print estunam.facultad




    def ser_activo(self):
          print 'eres alumno o exalumno'
          print '1. alumno'
          print '2.exalumno'
          m=int(input('elige una opcion: '))
          estunam.ingresar(m)          


    def Edad(self,nc,opcion):
         ed=int(input('ingresa tu edad: '))
         self.edad=ed
         print 'Edad actual:',  self.edad
         if opcion==1:
             a=self.edad-(2018-nc)+5
             print "Edad de egreso: ", a
         else:
             s=int(input ('Hace cuanto a;os egresaste'))
             e=self.edad-s
             print "Edad de egreso: ", e
               
 


    def ingresar(self,m):    
         nc=int (input('a;o de ingreso: '))
         self.ingreso=nc
         opcion=m
         print "a;o de Ingreso: ", self.ingreso   
         estunam.egresar(self.ingreso)    
         estunam.semcursados(self.ingreso,opcion)
         estunam.Edad(self.ingreso,opcion)         

         
    def egresar(self, nc):
          eg=nc+5
          print 'a;o de egreso: ', eg
     

    def semcursados(self,nc,opcion):
        if opcion==1:
             a=2*(2019-nc)-1
             print 'numero de semestres cursados: ', a
        else:
             print 'numero de semestres cursados: 10 o mas'
                   


estunam=Estudiante()
estunam.imprimir()
estunam.ser_activo()





