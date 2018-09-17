
# coding: utf-8

# In[ ]:


Saldo=0
operacion="si";
while (operacion=="si"):
	operacion = raw_input("INGRESE: deposito O retiro SEGUN LA OPERACION QUE DESEE REALIZAR")
	if (operacion == "retiro"):
		cantidad = input("Ingrese la cantidad que desea retirar de su cuenta: $")
		if (cantidad <= Saldo):
			Saldo = Saldo - cantidad
			print "Se realizo de manera exitosa el retiro. su saldo es: $",Saldo
		else:
			print "No tiene cantidad suficiente para retirar, vuelva a intentarlo."
	if (operacion == "deposito"):
		deposito = input("Ingrese la cantidad a depositar: $")
		Saldo = Saldo + deposito
		print "Se realizo deposito, en su cuenta tiene disponible ahora: $",Saldo
	operacion = raw_input("Desea realizar otra operacion? si/no: ")
print "Saldo total: $",Saldo

