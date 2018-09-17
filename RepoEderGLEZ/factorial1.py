
# coding: utf-8

# In[ ]:


def factorial(x,n):
    
	if(n>0):
		
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x
 
try:
	numero = int(raw_input("inserta un numero "))
 

	calculo=factorial(1,numero)
	print "El factorial de %s es %s" % (numero,calculo)
except:
	print "\nTiene que ser un valor numerico"

