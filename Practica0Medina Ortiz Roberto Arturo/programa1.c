//Elaborado por Medina Ortiz Roberto Arturo
//Convierte de grados Kelvin a Farenheit

#include<stdio.h>
float temperatura;

int main(int argc, char* argv[])
{
	printf("Ingresa la tempreatura en grados Kelvin\n");
	scanf("%f",&temperatura);
	temperatura=(temperatura*1.8)-459.67;
	printf("\nLa temparatura es igual a %f grados Farenheit",temperatura);
	getchar();
	getchar();
	return 0;
	
}
