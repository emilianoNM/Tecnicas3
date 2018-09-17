def burbuja(empresas): 
  temp=0
  for j in range(1,len(empresas)):
    for i in range(0,len(empresas)-j):
      if (empresas[i]>empresas[i+1]):
        temp=empresas[i]
        empresas[i]=empresas[i+1]
        empresas[i+1]=empresas[i]
        empresas[i+1]=temp


print "ordenamiento burbuja "
print "Rodriguez Miranda Omar"
empresas=["hp","Sony","Audi","Adidas","Cannon","DHL","Wish","Victorinox","Asimov"] 
print empresas
burbuja(empresas)
print "Ordenando alfabeticamente: "
print empresas 
