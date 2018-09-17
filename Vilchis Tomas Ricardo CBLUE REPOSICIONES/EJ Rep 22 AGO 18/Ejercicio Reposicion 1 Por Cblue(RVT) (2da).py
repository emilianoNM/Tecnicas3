
# coding: utf-8

# In[1]:


#Programa que lea del usuario 3 valores float (no cero) y que determine si pueden representar los lados de un triangulo"
#Creado por CBLUELENNON (RVT)


# In[2]:


print("Ingrese sus tres valores tipo float")
x=float(input("Primer valor\n"))
y=float(input("Segundo valor\n"))
z=float(input("Tercer valor\n"))


# In[3]:


if((x+y)>z): 
    condicion=1 
elif(): 
    condicion=0 
if((x+z)>y):
    condicion=condicion+1 
elif(): 
    condicion=0 

if((y+z)>x): 
    condicion=condicion+1 
elif():
    condicion=0

if(condicion==3): 
    print("SI EXISTE UN TRIANGULO CON ESTOS VALORES")

