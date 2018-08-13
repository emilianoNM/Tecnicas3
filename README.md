# Tecnicas3
Clase de Tecnicas de programación 
Rogelio Cabrera Murguía grupo 4
/* Programa: Menú calculadora de números enteros */

#include <conio.h>
#include <stdio.h>

int main()
{
    char opcion;
    int n1, n2;

    do
    {
        printf( "\n   >>> MENU CALCULADORA <<<" );
        printf( "\n\n   1. Sumar dos n%cmeros.", 163 );
        printf( "\n   2. Restar dos n%cmeros.", 163 );
        printf( "\n   3. Multiplicar dos n%cmeros.", 163 );
        printf( "\n   4. Dividir dos n%cmeros.", 163 );
        printf( "\n   5. Salir.\n" );

        /* Filtramos la opción elegida por el usuario */
        do
        {
            printf( "\n   Introduzca opci%cn (1-5): ", 162 );
            fflush( stdin );
            scanf( "%c", &opcion);

        } while ( opcion < '1' || opcion > '5' );
        /* La opción sólo puede ser '1', '2', '3', '4' o '5' */

        switch ( opcion )
        {
                      /* Opción 1: Sumar */
            case '1': printf( "\n   Introduzca primer sumando: " );
                      scanf( "%d", &n1);
                      printf( "\n   Introduzca segundo sumando: " );
                      scanf( "%d", &n2);
                      printf( "\n   %d + %d = %d\n", n1, n2, n1 + n2 );
                      break;

                      /* Opción 2: Restar */
            case '2': printf( "\n   Introduzca minuendo: " );
                      scanf( "%d", &n1);
                      printf( "\n   Introduzca sustraendo: " );
                      scanf( "%d", &n2);
                      printf( "\n   %d - %d = %d\n", n1, n2, n1 - n2 );
                      break;

                      /* Opción 3: Multiplicar */
            case '3': printf( "\n   Introduzca primer operando: " );
                      scanf( "%d", &n1);
                      printf( "\n   Introduzca segundo operando: " );
                      scanf( "%d", &n2);
                      printf( "\n   %d * %d = %d\n", n1, n2, n1 * n2 );
                      break;

                      /* Opción 4: División entera */
            case '4': printf( "\n   Introduzca dividendo: " );
                      scanf( "%d", &n1);
                      printf( "\n   Introduzca divisor: " );
                      scanf( "%d", &n2);
                      if ( n2 != 0 )
                          printf( "\n   %d div %d = %d ( Resto = %d )\n", n1, n2, n1 / n2, n1 % n2 );
                      else
                          printf( "\n   ERROR: No se puede dividir entre cero.\n" );
        }

    } while ( opcion != '5' );

    return 0;
}
