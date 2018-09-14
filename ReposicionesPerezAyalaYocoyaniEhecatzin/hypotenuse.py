import numpy as np

def hyutenuse(lado1, lado2):
	return np.sqrt((lado1**2+lado2**2))

def main():
	print("Hipotenusa triangulo 1 es: "+str(hyutenuse(3,4)))
	print("Hipotenusa triangulo 2 es: "+str(hyutenuse(5,12)))
	print("Hipotenusa triangulo 3 es: "+str(hyutenuse(8,15)))

main()