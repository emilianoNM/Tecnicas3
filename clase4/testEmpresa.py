#Empresas test
import Empresas

testEmpresa=Empresas.UnidadEconomica 
('Asimov','Tecnologica',
	'Asimov Ingenieria SA de CV')

if(testEmpresa.nombre=='Asimov'):
	print 'test de nombre correcto'
else: 
	print 'test de nombre error'

print testEmpresa.tipo

print testEmpresa.razonSocial
