class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, id,padre):
		super(Nodo, self).__init__()
		self.id = id
		self.padre=padre
		self.hijos=[]
		if padre!=None:
			padre.addHijo(self)

	def addHijo(self,hijo):
		self.hijos.append(hijo)
		hijo.padre=self
	def esHoja(self):
		return len(self.hijos)==0
	def delete(self):
		if(self.esRaiz()):
		   pass
		else:
		   padre=self.padre
		   hijos=padre.getHijos()
		   hijos.remove(self)
		   self.padre=None

	def esRaiz(self):
		return self.padre==None
	def getHijos(self):
		return self.hijos
	def __str__(self):
		return self.id 
	def __repr__(self):
		return self.id

class ArbolBinario(object):
	"""docstring for ArbolBinario"""
	def __init__(self, nodo):
		super(ArbolBinario, self).__init__()
		if(nodo.esRaiz()==False):
			raise ValueError('El nodo %s no es una raiz '%(nodo))
		self.__raiz__ = nodo

	def addNodo(self,nodo):
			aux=self.__raiz__
                        aux1=aux.gethijos
                         if len(aux1<2):
                             aux1.addHijo(nodo)
                
                        hijois=aux1.getHijos()
		        for i in hijos:
				    if i.esHoja():
					hijo.addHijo(nodo)
					return 
					   for i in hijos:
						if len(i.getHijos()!=2):
							hijo.addHijo(nodo)
						return
					    


	def __str__(self):
			pass	

