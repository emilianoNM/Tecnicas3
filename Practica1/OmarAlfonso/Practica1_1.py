class Planetas:
    Masa=10
    Dias=365
    Habitable=True

    def __init__(self, Masa, Dias, Habitable):
        self.Masa=Masa
        self.Dias=Dias
        self.Habitable=Habitable

    def __init__(self):
        self.Masa = 10
        self.Dias = 365
        self.Habitable = False

    def Año(self):
        print("son", self.Dias, "Dias")

    def CambiarMasa(self, dM):
        self.Masa=self.Masa+dM
        print("Nueva MAsa", self.Masa)

    def Destruir(self):
        self.Habitable=False
        print("El planeta ya no es Habitable")

    def Terrormar(self):
        self.Habitable=True
        print("El planeta ya es Habitable")

    def CambiarDias(self, NuevosDias):
        self.Dias=NuevosDias
        print("Ahora los años son de", self.Dias,"Dias" )

    def Datos(self):
        print("Masa", self.Masa)
        print("Año",self.Dias)
        print("Habitable",self.Habitable)



