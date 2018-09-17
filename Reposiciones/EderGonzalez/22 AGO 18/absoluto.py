
# coding: utf-8

# In[ ]:


def absoluto(num):

	if num<0:
		return (num*(-1))
	else:
		return num

x=input("Ingrese el numero a evaluar: ")
print "\n""El valor absoluto del numero es: ", absoluto(x)

