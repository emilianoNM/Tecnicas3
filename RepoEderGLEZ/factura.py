
# coding: utf-8

# In[ ]:


def main():
 
    print "ELIJA EL PRODUCTO DESEADO"

    print "SELECCION"

    print "CAMISA........................... 1"
    print "CINTURON......................... 2"
    print "ZAPATOS.......................... 3"
    print "PANTALON......................... 4"
    print "CALCETINES....................... 5"
    print "FALDAS........................... 6"
    print "GORRAS........................... 7"
    print "SUETER........................... 8"
    print "CORBATA.......................... 9"
    print "CHAQUETA......................... 10"

    relacion = {1:35, 2:10, 3:50, 4:40, 5:5, 6:20, 7:7, 8:15, 9:10, 10:35}
     
    codigo = input("INTRODUZCA EL CODIGO: ")
    
    print "EL PRECIO ES: $", relacion[codigo]
    cantidad = input("INTRODUZCA EL NUMERO DE UNIDADES: ")
    
     
    precio_t = float(relacion[codigo] * cantidad)
     
    print "EL TOTAL A PAGAR ES: $", precio_t
     
main()

