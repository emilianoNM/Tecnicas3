
# coding: utf-8

# In[ ]:


class PilaEmpresa:
    def __init__(self):
        self.info = []
    def Completa(self):
        return self.info == []
    def push(self,item):
        self.info.insertar(0,info)
    def pop(self):
        return self.info.pop(0)
    def size(self):
        return len(self.info)
    def __str__(self):
        return "Pila: {}".format(self.info)

a = PilaEmpresa()
print (a.pop())
a.push(4)
print(a.Completa())
print(a.size())
print(a)

