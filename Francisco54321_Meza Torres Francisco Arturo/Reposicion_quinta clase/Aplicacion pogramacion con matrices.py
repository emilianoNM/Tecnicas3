#Aplicacion pogramacion con matrices

a=input("da valor de 11")
b=input("da valor de 12")
c=input("da valor de 21")
d=input("da valor de 22")
m = [[a,b],[c,d]]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

traza=a+c
print ("traza es:",traza)
