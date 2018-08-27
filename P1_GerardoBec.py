#GerardoBecerra

class Dron:
    Tvuelo=10
    Estructura='plastico'
    Tipo:'fotografia'
    Motores= 4
    Color= 'negro'
    Tamaño='pequeño'
    Bateria=100
            
    
    def __init__(self, Tvuelo, Estructura, Tipo):
        self.Tvuelo=Tvuelo
        self.Estructura=Estructura
        self.Tipo=Tipo
        self.Motores=Motores
        self.Color=Color
        
    
    def bateriabaja(self):
        print("La bateria esta baja")
        self.Motores=self.Motoresbajos
        print("Motores con el 10% de bateria", self.Motores)

    def niveldebateria(self):
        if(self.Bateria!=100):
            print("El nivel de bateria es:")
            self.Bateria=self.Bateria-50
        elif(self.Bateria==50):
            print("La bateria esta a la mitad") 
        elif(self.Bateria==10):
            print("Cargar bateria")        
    
    def motordañado(self):
        print("El motor esta dañado")
        self.Motores=False
	self.Motores=True 

    def estructura(self):
        print("La estructura del Dron es de plastico")
        self.Estructura=False
	self.Estructura=True                
        
    def Tipo(self):
        print("El dron es de fotografia?")
        if(self.Tipo=='fotografia'):
            self.Tipo=True
        elif(self.Tipo!='carrera'):
            print("Dron equivocado")
            self.Tipo=False
        elif(self.Tipo!='riego'):
            print("Dron equivocado")
            self.Tipo=False
            
    def info Dron(self):
        print("Tiempo de Vuelo",self.Tvuelo)
        print("Tipo de Dron",self.Tipo)
        print("Nivel de bateria",self.Bateria)
        print("Numero de motores",self.Motores)
        print("Estructura del Dron",self.Estructura)

