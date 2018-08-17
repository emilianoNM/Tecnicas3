#include<stdio.h>
int main(int argc,char* argv[])
{
	float x[7]={1,1.8,2,2.5,3,5,15.3};
	float y[7]={1,1.5,2.5,2.8,4,6,17.8};
	float xy, x2,sx,sy;
	int conde;
	xy=0;
	for (conde=0;conde<7;conde++)
	{
		xy=xy+(x[conde]*y[conde]);
	}
	sx=0;
	for (conde=0;conde<7;conde++)
	{
		sx=sx+x[conde];	
	}
	sy=0;
	for (conde=0;conde<7;conde++)
	{
		sy=sy+y[conde];
	}
	x2=0;
	for (conde=0;conde<7;conde++)
	{
		x2=x2+(x[conde]*x[conde]);
	}
	float m,b;
	
	m=(7*xy-(sx*sy))/((7*x2)-(sx*sx));
	b=(sy-(m*sx))/(7);
	
	printf("\nLa formula de regresión es:\n\t %.3gx+%.3g",m,b);
	getchar();
	return 0;
	
}

