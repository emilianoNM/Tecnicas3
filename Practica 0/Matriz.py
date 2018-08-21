import numpy as np
def Menu():
    print """************
Matriz 2x2
************
Menu
1) Llenar matriz
2) Mostrat matriz
3) Transponerla
4) Traza
5) Determinante 
6) Salir"""
def Matriz():
    print "presione enter cada que seleccione un valor o desee continuar con el proceso"
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <6):
        if (opc==1):
	      n1 = int(input("Primer numero:"))
	      n2 = int(input("Segundo numero:"))
              n3 = int(input("Tercer numero"))
              n4 = int(input("Cuarto numero"))
              A = np.array([[n1, n2],
              		    [n3, n4]])
        elif(opc==2):
            print A
           
        elif(opc==3):
            B=np.transpose(A)
	    print B
        elif(opc==4):
           tragi=np.trace(gi)
	   print tragi
          
        elif(opc==5):
            B=np.linalg.det(A)
	    print B
	elif(opc==6):
	    opc=-1
              
	opc = int(input("Selecione Opcion\n"))
Matriz()
