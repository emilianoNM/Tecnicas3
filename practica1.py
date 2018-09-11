
print Pacheco Rios Jesus.

class Guitarra:
    Ncuerdas=5
    Cuerpo='madera'
    Tipo:'semihollow
    Cuerdas:'metalicas'
    Calidad=10
        
    
    def __init__(self, Ncuerdas, Cuerpo, Tipo):
        self.Ncuerdas=Ncuerdas
        self.Cuerpo=Cuerpo
        self.Tipo=Tipo
        self.Cuerdas=Cuerdas
        self.Calidad=Calidad
        
    
    def cuerdarota(self):
        print("Se ha roto una cuerda :´o")
        self.Ncuerdas=self.Ncuerdas-1
        print("El nuevo numero de cuerdas es:", self.Ncuerdas)
        
    
    def cuerdasNylon(self):
        print("Se han cambiado las cuerdas metalicas a cuerdas de nylon")
        self.Cuerdas=False
        
        
    def guitarraRota(self):
        if(self.Calidad!=10):
            print("La guitarra no se escucha bien")
            self.Calidad=self.Calidad-5
        elif(self.Calidad==10):
            print("La guitarra esta en perfecto estado")
            
        
    def Tipo(self):
        print("La guitarra es tipo semihollow?")
        if(self.Tipo=='semihollow'):
            self.Tipo=True
        elif(self.Tipo!='semihollow'):
            print("La guitarra es de otro tipo")
            self.Tipo=False
            
    def resumen(self):
        print("Num de cerdas",self.Ncuerdas)
        print("Calidad de guitarra",self.Calidad)
        print("¿Tiene cuerdas metalicas?",self,Cuerdas)
        print("Es semihollow?",self.Tipo)
    
    #Por Pacheco Rios Jes{us}