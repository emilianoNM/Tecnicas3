#complejos
def suma(a1,a2,b1,b2):
  sr=a1+a2
  si=b1+b2
  print "el resultado de la suma es: "
  mostrar_r(sr,si)

def resta(a1,a2,b1,b2):
  rr1=a1-a2
  ri1=b1-b2
  print "el resultado de la resta Z1-Z2 es: "
  mostrar_r(rr1,ri1)
  rr2=a2-a1
  ri2=b2-b1
  print "el resultado de la resta Z2-Z1 es: "
  mostrar_r(rr2,ri2)


def mult(a1,a2,b1,b2):
  print "el resultado de la multiplicacion: "
  print (a1-a2),"-",(b1-b2),"i"

def mostrar_r(a,b):
  if(b<0):
   print a,b,"i"
  else:
    print a,"+",b,"i" 


def m(a1,a2,b1,b2):
  if (b1<0 and b2<0):
   print "Z1=",a1,b1,"i"
   print "Z2=",a2,b2,"i"
  if(b1<0 and b2>0):
    print "Z1=",a1,b1,"i"
    print "Z2=",a2,"+",b2,"i"
  if(b1>0 and b2<0):
    print "Z1=",a1,"+",b1,"i"
    print "Z2=",a2,b2,"i"  
  if(b1>0 and b2>0):
    print "Z1=",a1,"+",b1,"i"
    print "Z2=",a2,"+",b2,"i"

print " Suma y resta de numeros complejos"
print "Ingresa el primer numero complejo"
a1=input("parte real: ")
b1=input("parte imaginaria: ")

print "Ingresa el segundo numero complejo"
a2=input("parte real: ")
b2=input("parte imaginaria: ")

opc=input("1.suma  2.resta") 
if(opc==1):
   m(a1,a2,b1,b2)
   suma(a1,a2,b1,b2)

if(opc==2):
   m(a1,a2,b1,b2)
   resta(a1,a2,b1,b2)


