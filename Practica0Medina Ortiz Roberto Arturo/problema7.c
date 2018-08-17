//Medina Ortiz Roberto Arturo

#include<stdio.h>

int main(int argc,char* argv[])
{
	float volumen;
	int tiempo;
	int k=1800;
	printf("Ingresa el tiempo: ");
	scanf("%d",&tiempo);
	volumen=k/(30+(2*tiempo));
	printf("\n El volumen en %d seg es: %.3g cm^3",tiempo,volumen);
	getchar();
	getchar();
	return 0;
	
}
