
#Pacheco Rios Jes{us}

from  Estudiante import Estudiante 

class Ingeniero(Estudiante):
    
    def __init__(self, nombre, materias, escuela, division, carrera):
        
        Estudiante.__init__(self, nombre, materias, escuela)
        self.divison = division
        self.carrera = carrera
    
    def getDivision(self):
        return self.divison
    
    def getCarrera(self):
        return self.carrera
    
    def setDivision(self, division):
        self.divison = division
    
    def setCarrera(self, carrera):
        self.carrera = carrera