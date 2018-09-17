
# coding: utf-8

# In[ ]:




L_l = [1,34.5,35,98,'c ','d',78,234.67,'rt ',45,222,978,4e9]
L_nl = [] #Creacion de lista con datos numericos solamente

for q in L_l:
    if type(q)!=str:
        L_nl .append (q)
        
print ("Datos numericos: ",L_nl)

#busqueda del maximo 
My_max = L_n1 [0]

for q in L_nl [l:]: 
    if q>My_max:
        My_max = q

print ("Maximo numerico: ",My_max)
#print ("Usando max (L_inicial): ",max(L_l)) 
print ("Usando max(L_numeros): ",max (L_nl))

