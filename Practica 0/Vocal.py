frase =raw_input("Introduce una cadena: ")
cont=0
for x in range(0,len(frase)):
	if (frase[x]=='a'or frase[x]=='A' or frase[x]=='e' or frase[x]=='E' or frase[x]=='i' or frase[x]=='I' or frase[x]=='o' or frase[x]=='O' or frase[x]=='u' or frase[x]=='U'):
		cont=cont+1


print "Tu frase tiene " + str(cont) +" vocales"
