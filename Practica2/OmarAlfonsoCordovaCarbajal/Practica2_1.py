import copy

class Telefono:

    def __init__(self, Marca, Numero, Provedor):
        self.Marca=Marca
        self.Numero=Numero
        self.Provedor=Provedor

    def getMarca(self):
        return self.Marca

    def getNumero(self):
        return self.Numero

    def getProvedor(self):
        return self.Provedor

    def setMarca(self, Marca):
        self.Masa=Marca

    def setNumero(self, Numero):
        self.Numero=Numero

    def setProvedor(self, Provedor):
        self.Provedor=Provedor

class Celular(Telefono):
    def __init__(self, Camara):
        self.Camara=Camara

    def getCamara(self):
        return self.Camara

    def setCamara(self, Camara):
        self.Camara=Camara


Tel=Telefono("Hawaii", 11111, "Telcel")
print(Tel.getMarca(), Tel.getNumero(), Tel.getProvedor())
Cel=copy.deepcopy(Tel)
Cel.__class__=Celular
Celular.__init__(Cel, "20 Megapixeles")

print (Cel.getNumero(), Cel.getProvedor(), Cel.getMarca(), Cel.getCamara())

