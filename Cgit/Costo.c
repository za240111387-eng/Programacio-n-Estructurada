#include <stdio.h>

int main() {
     float a;
     float b;
    float result;


    printf("la cantidad de productos es ");
    scanf("%f",&a);
     printf("el precio unitario es ");
    scanf("%f",&b);
    result = a * b;

    printf("el costo total es %.2f\n",result);

    return 0;
}
