
#Pacheco Rios Jes{us}

import Ingeniero as ing

if __name__ == '__main__':
    yo = ing.Ingeniero(Jesus,["Tecnicas de Programación", "Ingenieria de Manufactur"],"FI UNAM", "DIMEI", "Mecatrónica")
    
    print(yo.getNombre(), yo.getMaterias(), yo.getEscuela())
    yo.setNombre("CANDIDO")
    yo.setMaterias(["Cálculo Vectorial","Ecuaciones Diferenciales"])
    yo.setEscuela("FI UNAM II")
    yo.setDivision("DIMEI")
    yo.setCarrera("Industrial")
    print(yo.getNombre(), yo.getMaterias(), yo.getEscuela(), yo.getDivision(), yo.getCarrera())