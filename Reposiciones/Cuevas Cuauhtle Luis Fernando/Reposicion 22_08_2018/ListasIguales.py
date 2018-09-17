#Programa que compara tres listas y te dice si son iguales o desiguales entre ellas

Lista1 = [10, 10, 0, 0, 10]
Lista2 = [10, 10, 10, 0, 0]
Lista3 = [1, 10, 10, 0, 0]

print("Lista 1:\n")
for x in range(len(Lista1)): 
    print Lista1[x],
print("\n")
print("Lista 2:\n")
for x in range(len(Lista2)): 
    print Lista1[x], 
print("\n")
print("Lista 3:\n")

for x in range(len(Lista2)): 
    print Lista1[x], 
print("\n")
print('Comparando la Lista 1 y la Lista 2')
print("Las listas son iguales?")
print(' '.join(map(str, Lista2)) in ' '.join(map(str, Lista1 * 2)))
print("\n")
print('Comparando la Lista 1 y la Lista 3')
print("Las listas son iguales?")
print(' '.join(map(str, Lista3)) in ' '.join(map(str, Lista1 * 2)))

 

