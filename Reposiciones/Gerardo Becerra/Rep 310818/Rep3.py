
# coding: utf-8

# In[ ]:


def print_asegundos ( horas , minutos , segundos) :
    
    segsal = 3600 * horas + 60 * minutos  + segundos 
    print "Son ",segsal, "segundos"

def main ( ) :
    for x  in  range (3) :
    hs  =  raw_input ( "Cuantas  horas? :  ")
    min = raw_input ( "Cuantos minutos? : ")
    seg = raw_input ( "Cuantos segundos? : ") 
    print_asegundos ( hs, min , seg)
 
   
main ( )
 


