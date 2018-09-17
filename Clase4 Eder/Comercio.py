
# coding: utf-8

# In[ ]:


class Comercio(object):
	Length=0
	def __init__(self,nombreProducto,nombreProvedor,nombreComerciante,establecimiento,mediodeDistribucion,numIdenFiscal,sectordeComercio,superficiedeVenta,telefono,email):
		self.nombreProducto= nombreProducto
		self.nombreProvedor= nombreProvedor
		self.nombreComerciante = nombreComerciante
		self.establecimiento= establecimiento
		self.mediodeDistribucion= mediodeDistribucion
		self.numIdenFiscal= numIdenFiscal
		self.sectordeComercio= sectordeComercio
		self.superficiedeVenta= superficiedeVenta
		self.telefono= telefono
		self.email= email

