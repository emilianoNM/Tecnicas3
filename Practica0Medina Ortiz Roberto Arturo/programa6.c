#include<stdio.h>
int main()
{
	int conde=2;
	int contar=2;
	do
	{
		
		conde=conde+3;
		printf("%d ",conde);
		contar=contar+conde;
		if(conde<1800)
		{
			conde=conde+2;
			printf("%d ",conde);
			contar=contar+conde;

		}
	}
	while(conde<1800);
	printf("\n%d ",contar);
}
