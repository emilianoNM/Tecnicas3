
#Pacheco Rios Jes{us}

def burbuja(empresas): 
  temp=0
  for j in range(1,len(empresas)):
    for i in range(0,len(empresas)-j):
      if (empresas[i]>empresas[i+1]):
        temp=empresas[i]
        empresas[i]=empresas[i+1]
        empresas[i+1]=empresas[i]
        empresas[i+1]=temp
        print (empresas)


#print "El orden correcto es: "
#print empresas 


print "ordenamiento burbuja "
print "Linares Alonso Joshua A."
empresas=["Lenovo","Telcel","Banamex","Google","Asimov"] 
burbuja(empresas)
print "El orden correcto es: "
print empresas 