//Medina Ortiz Roberto Arturo

#include<stdio.h>
int main(int argc,char* argv[])
{
	float conde;
	float suma=0;
	float producto;
	
	for(conde=0;conde<=15;conde++)
	{
		producto=1/(conde+1);
		suma=suma+producto;
	}
	printf("El resultado es: %f",suma);
	getchar();
	return 0;
}
