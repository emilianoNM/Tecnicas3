
# coding: utf-8

# In[ ]:


from  Drones import Drones 

class Clasificacion(Drones):
    
    def __init__(self, bateria, peso, tvuelo, tipo, motores):
        
        Estudiante.__init__(self, bateria, peso, tvuelo)
        self.tipo=tipo
        self.motores=motores
    
    def getTipo(self):
        return self.tipo
    
    def getMotores(self):
        return self.motores
    
    def setTIpo(self, tipo):
        self.tipo=tipo
    
    def setMotores(self, motores):
        self.motores=motores

