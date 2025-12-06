#include <stdio.h>

int main() {
    float iva=1.16;
    float a;
    float costo;
    printf("ingresa el valor del producto ");
    scanf("%f",&a);

    costo = iva * a ;
    printf("el total es %f\n",costo);
    return 0;
}
