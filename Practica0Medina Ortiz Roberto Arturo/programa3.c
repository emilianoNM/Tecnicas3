//Elaborado por Medina Ortiz Roberto Arturo

#include<stdio.h>
int conde, contar;
int matriz[2][2];
int menu;
int capturar()
{
	for (conde=1;conde<=2;conde++)
	{
		for (contar=1;contar<=2;contar++)
		{
			printf("\n Ingresa el valor %d, %d: ",conde, contar);
			scanf("%d",&matriz[conde][contar]);
		}
	}
	printf("\n Se ha capturado la matriz");
	getchar();
	getchar();
	return 0;
}
int mostrar()
{
	for (conde=1;conde<=2;conde++)
	{
		
		for (contar=1;contar<=2;contar++)
		{
			printf(" %d",matriz[conde][contar]);
			
		}
		printf("\n");
	}
}
int traspuesta()
{
	for (contar=1;contar<=2;contar++)
	{
		
		for (conde=1;conde<=2;conde++)
		{
			printf(" %d",matriz[conde][contar]);
			
		}
		printf("\n");
	}
}
int traza()
{
	return matriz[1][1]+matriz[2][2];
}
int determinante()
{
	int detp1, detp2;
	detp1=(matriz[1][1]*matriz[2][2]);
	detp2=(matriz[1][2]*matriz[2][1]);
	return detp1-detp2;
}

int main(int argc, char* argv[])
{
	int trasa,det;
	do
	{
		printf("¿Que quiere hacer?");
		printf("\n1. Capturar matriz");
		printf("\n2. Mostrar matriz");
		printf("\n3. Mostrar matrz traspuesta");
		printf("\n4. Calcular la traza");
		printf("\n5. Calcular el determinante");
		printf("\n6. Salir\n\t"); 
		
		scanf("%d",&menu);
		
		switch(menu)
		{
			case 1:
				printf("entre\n");
				capturar();
				break;
			case 2:
				mostrar();
				break;
			case 3:
				traspuesta();
				break;
			case 4:
				
				trasa=traza();
				printf("\nLa traza de la matriz es: %d\n",trasa);
				break;
			case 5:
				det=determinante();
				printf("\nEl determinante de la matriz es: %d\n",det);
				break;
			case 6:
				break;
			default:
				printf("\n\tNo se pudo, ingresa opcion valida");
				break;
		}
	}
	while(menu!=6);
	
	getchar();
	getchar();
	return 0;
			
	
}
