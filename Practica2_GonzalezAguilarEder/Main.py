
# coding: utf-8

# In[ ]:


import Ingeniero as ing

if __name__ == '__main__':
    yo = ing.Ingeniero("Yocoyani",["Tecnicas de Programación", "Ingenieria de Materiales"],"FI UNAM", "DIMEI", "Mecatrónica")
    
    print(yo.getNombre(), yo.getMaterias(), yo.getEscuela())
    yo.setNombre("Juan")
    yo.setMaterias(["Cálculo Vectorial","Ecuaciones Diferenciales"])
    yo.setEscuela("FI UNAM II")
    yo.setDivision("DIE")
    yo.setCarrera("Computación")
    print(yo.getNombre(), yo.getMaterias(), yo.getEscuela(), yo.getDivision(), yo.getCarrera())
    
    

