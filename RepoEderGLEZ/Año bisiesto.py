
# coding: utf-8

# In[ ]:


print("Comprobador de anios bisiestos")
fecha = int(input("Escriba un anio: "))
def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)
 if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print( fecha, "es bisiesto.")
print("Comprobador de anios bisiestos")
fecha = int(input("Escriba un anio, el programa indicará su naturaleza: "))
if es_bisiesto(fecha):
    print(fecha, "es un año bisiesto.")
else:
    print( fecha, "no es bisiesto.")
    print(fecha, "no es un año bisiesto.")

