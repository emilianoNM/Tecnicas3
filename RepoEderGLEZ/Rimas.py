
# coding: utf-8

# In[ ]:


uno = raw_input ("Dime la primera palabra: ")

dos = raw_input ("Dime la segunda palabra: ")

if len(uno) < 3 or len(dos) < 3:
 print "Las palabras tienen menos de 3 letras"

elif uno[-3:] == dos[-3:]:
 print "Riman"
 
else:
 print "No riman"
 

