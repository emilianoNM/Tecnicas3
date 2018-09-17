// Ejercicio 3

#include<iostream> 
using namespace std; 

main() 
{ 
int i,j,k,l,m,n ; 
float a[100][100]; 
float det; 
cout << "Introducir el ORDEN DE LA MATRIZ : N = " << endl; 
cin >> n; 
m=n-1; 
/* Vamos a introducir la matriz por teclado*/ 

cout << "Introducir los elementos" << endl; 
cout << "------------------------" << endl;; 
for(i=1;i<=n;i++) 
{ for(j=1;j<=n;j++) 
{cin >> a[i][j];}} 
/* SI QUEREMOS LEER LOS ELEMENTOS DE LA MATRIZ LISTADOS */ 

/*for(i=1;i<=n;i++) 
{ for(j=1;j<=n;j++) 
printf("\t\t\tA(%d,%d) =%8.4f\n",i,j,a[i][j] ); }*/ 

/*****Calculo del DETERMINANTE*****/ 
det=a[1][1]; 
for(k=1;k<=m;k++) 
{ l=k+1; 
for(i=l;i<=n;i++) 
{ for(j=l;j<=n;j++) 
a[i][j] = ( a[k][k]*a[i][j]-a[k][j]*a[i][k] )/a[k][k]; } 
det=det*a[k+1][k+1]; 
} 
cout << endl; 
cout << "DETERMINANTE = " << det << endl; 
cout << "------------------------" << endl; 

system("PAUSE"); 

return 0; 
}


// Ejercicio 5 

#include <stdio.h>
#include <math.h>
int main()
{
   float a,b,c;
   printf("Ingresa coeficiente cuadratico\n");
   scanf("%f",&a);
   printf("Ingresa coeficiente lineal\n");
   scanf("%f",&b);
   printf("Ingresa constante\n");
   scanf("%f",&c);
   double disc=pow(b,2)-4*a*c;
    if(a!=0){
          if(disc<0){
          printf("Tiene raices imaginarias");
          }else{
          double x1=(-b+sqrt(disc))/(2*a);
          double x2=(-b-sqrt(disc))/(2*a);
          printf("X1 = %lf X2 =%lf",x1,x2);
        }
      }else{
     printf("El coeficiente cuadratico debe ser diferente de 0");
      }
   return 0;
}

// Ejercicio 9

#include<stdio.h>
#include<stdlib.h>
int main(){
    int i,n;
    float x,y,sumx,sum_sqx,sumy,sumxy,a,b;
    printf("\n Numero de datos: ");
    scanf("%d",&n);
    sumx =0;
    sum_sqx =0;
    sumy=0;
    sumxy=0;
     for(i=0;i<n;i++){
   printf("X: ");
   scanf("%f",&x);
   printf("Y: ");
   scanf("%f",&y);
   sumx = sumx +x;
   sum_sqx = sum_sqx + (x*x);
   sumy= sumy + y;
   sumxy = sumxy + (x*y);
   }
    b = (sumxy-(sumx*sumy)/n)/(sum_sqx-(sumx*sumx)/n);
    a = (sumy/n)-(b*sumx/n);
    printf("\nEcuacion lineal: Y= %f + %fX\n",a,b);
    system("pause");
    return 0;
 }