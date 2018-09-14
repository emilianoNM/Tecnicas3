#Razon social de la empresa

class RazonSocial(object):
    def __init__(self, Individual, SociedadColectiva, SociedadAnonima, SociedadResponsable, 
    	SociedadComanditaria, EmpresaUnipersonal, SociedadAnonimaCerrada):
		self.Individual=Individual
		self.SociedadColectiva=SociedadColectiva
		self.SociedadAnonima=SociedadAnonima
		self.SociedadResponsable=SociedadResponsable
		self.SociedadComanditaria=SociedadComanditaria
		self.SociedadAnonimaCerrada=SociedadAnonimaCerrada
		self.EmpresaUnipersonal=EmpresaUnipersonal