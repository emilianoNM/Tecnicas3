###programa para sacar determinante de matris de 2*2 

print "Ingrese los valores:"
print "|a b|"
print "|c d|"
a = float(raw_input('Ingrese el valor a '))
b = float(raw_input('Ingrese el valor b '))
c = float(raw_input('Ingrese el valor c '))
d = float(raw_input('Ingrese el valor d '))

total=a*d-b*c

if total!=0:
   print " ",d/total,' ',-c/total;
   print " ",-b/total,' ',a/total;


else:
    print "Error el det. da 0";