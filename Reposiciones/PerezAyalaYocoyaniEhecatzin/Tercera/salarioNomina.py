# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:45:13 2018

@author: yocoy
"""

def lectura(nombreDato):
	while True:
		try: 
			print("Inroduce el "+ nombreDato)
			lectura = input("--> ")
			break
		except:
			print("Dato no valido")
	return lectura

def calculoNomina(salario, horas):
    return salario*horas

def main():
    
    decision = True
    print("Calculo de la nomina")
    
    while decision:
        nombre = input("Nombre del empleado: ")
        horasTrabajadas = lectura("Horas de trabajo")
        salario = lectura("salario por hora")
        print("Para "+str(nombre)+" su salario es de "+str(salario)+"por un trabajo de "+str(horasTrabajadas))
        print("\nIntroduce 1 para terminar ")
        dec = lectura("Decision")
        if dec == 1:
            break