x=miclase()
class Fraccion:
    def __init__(self,numerador,denominador):
        self.num = numerador
        self.den = denominador
        def mostrar(self):
     print(self.num,"/",self.den)
      miF = Fraccion(3,5)
      miF.mostrar()
      print(miF)
      print("hize", miF, " del pastel")
      def __str__(self):
      return str(self.num)+"/"+str(self.den)
     miF.__str__()
     str(miF)


     def __add__(self,pfraccion):
    neuenum = self.num*pfraccion.den + self.den*pfraccion.num
    neueoden = self.den * pfraccion.den
    comun = mcd(neuenum,neueden)
    return Fraccion(neuenum//comun,neueden//comun)


        
