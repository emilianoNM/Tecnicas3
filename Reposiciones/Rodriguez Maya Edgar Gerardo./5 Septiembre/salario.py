###programa para calcular salario

horas = input("Ingrese el numero de horas semanales: ")
pago = input("Ingrese el pago de la hora (regular): ")
extra= input("Ingrese el pago de la hora(extra):")
if horas > 40:
 	extras = horas - 40
        print 'El salario semanal es de:', 40 * pago + extras*extra
else:
        print 'El salario semanal es de:', horas * pago