#include<stdio.h>

int conde, contar=0;
char cadena[30],letra;

int buscar()
{
	contar=0;
	for(conde=0;conde<30;conde++)
	{
		if(letra==cadena[conde])
		{
			contar++;
		}
	}
	printf("\nSe encontro la letra %d veces",contar);
}
int main(int argc, char* argv[])
{
	
	
	printf("Introduzca una cadena\n");
	scanf(" %[^\n]",&cadena);
	printf("\n%s",cadena);
	
	do
	{
		printf("\nIntroduce una letra\n\t");
		getchar();
		scanf(" %[^\n]",&letra);
		buscar();
		printf("\nBuscar otra letra?\n[S]/[N]: ");
		getchar();
		scanf(" %[^\n]",&letra);
	}
	while(letra=='s'|| letra=='S');
	
	
	
}
