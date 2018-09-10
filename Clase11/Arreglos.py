#Arreglos
a=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]

print a

a.append(25)
print a 

b=['a','b','c','d','f']

a.append(b)
print type(b)


print b

print a[len(a)-1][3]


class Animal(object):
 	"""docstring for Animal"""
 	def __init__(self, arg):
 		super(Animal, self).__init__()
 		self.nombre = arg


a.append(Animal("colmillo blanco")) 

print a

a.extend(b)

print a

for c in b:
	a.append(c)

print a

a.insert(0,Animal("tigre"))

print a

a.sort()

print a

a.reverse()

print a 

print a.count('a')
a.remove('a')

print a.count('a')
print a 

print a.pop()

print a


for c in a:
	print c

while len(a)>0 :
	print a.pop()

print a


































#Tuplas 
