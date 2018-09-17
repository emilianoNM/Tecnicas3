
# coding: utf-8

# In[1]:


#Programa que indique en base a la calificacion de un alumno si este aprobo el curso o esta reprobado
#Por CBLUELENNON (RVT)


# In[2]:


print("Ingrese las califiacones de los 3 parciales realizados en el semestre")
a=int(input())
b=int(input())
c=int(input())
calificacionpromediofinal=(a+b+c)/3
if(calificacionpromediofinal>=6):
    print("EL ALUMNO APROBO ESTA MATERIA :D")
elif(calificacionpromediofinal<6):
    print("REROBADO HIJO :d")

