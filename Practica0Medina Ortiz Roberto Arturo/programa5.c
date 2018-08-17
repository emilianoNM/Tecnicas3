//Medina Ortiz Roberto Arturo
#include<stdio.h>
#include<math.h>
int main(int argc,char* argv[])
{
	int a,b,c;
	float disc;
	float x1,x2,x3,x4;
	char op;
	do
	{
		printf("Este programa calcula las raices de un polinomio de segundo grado");
		printf("\nPara el polinomio Ax^2+Bx+C");
		printf("\nIngresa el termino A: "); 
		scanf("%d",&a);
		printf("\nIngresa el termino B: ");
		scanf("%d",&b);
		printf("\nIngresa el termino C:");
		scanf("%d",&c);
		disc=pow(b,2)-(4*a*c);
		if(disc>=0)
		{
			x1=(-b+sqrt(disc))/2*a;
			x2=(-b-sqrt(disc))/2*a;
			
			printf("\n las raices son:\nx1= %.3f \nx2= %.3f",x1,x2);
		}
		else
		{
			x3=sqrt(-disc)/(2*a);
			x1=-b/(2*a);
			printf("\nLas raices son\nx1= %.3f + %.3fi\nx2= %.3f - %.3fi",x1,x3,x1,x3);
		}
		
		printf("\nOtra vez? [s/n] ");
		scanf("%s",&op);
		
		
	}
	while(op=='s');

	
	getchar();
	getchar();
	return 0;
}
