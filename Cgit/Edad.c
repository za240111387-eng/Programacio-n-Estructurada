#include <stdio.h>

int main() {
    int a;
    int b;
    int edad;
    printf("ingresa tu edad ");
    scanf("%d",&a);
    printf("ingresa el año actual");
    scanf("%d",&b);
    edad= b - a ;
    printf("tu año de nacimiento es %d\n",edad);
    return 0;
}
