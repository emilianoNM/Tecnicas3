
# coding: utf-8

# In[ ]:


def primo(x):

	for numeros in range(2,(x-1)):

		if x%numeros==0 and numeros!=x:
			break
		else:
			print "El numero es primo!"
			break
	return 

def par():
	x=input("Ingrese el numero a evaluar: ")

	if x%2==0:
		print "El numero es par"
	return x

num=par()
print 
primo(num)

