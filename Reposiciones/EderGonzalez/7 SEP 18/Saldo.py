
# coding: utf-8

# In[ ]:


horas = input("Inserte el numero de horas semanales: ")
precio = input("Inserte el precio de la hora (regular): ")
precioextra= input("Ingrese el precio de la hora(extra):")
if horas > 40:
 	hextra = horas - 40
        print 'El salario semanal es de:', 40 * precio + hextra*precioextra
else:
        print 'El salario semanal es de:', horas * precio

