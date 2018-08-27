
# coding: utf-8

# In[ ]:


class Estudiante(object):
    
    def __init__(self, nombre, materias, escuela):
        
        self.nombre = nombre
        self.materias = materias
        self.escuela = escuela
    
    def getNombre(self):        
        return self.nombre
    
    def getMaterias(self):
        return self.materias
    
    def getEscuela(self):
        return self.escuela
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setMaterias(self, materias):
        self.materias = materias
        
    def setEscuela(self, escuela):
        self.escuela = escuela

