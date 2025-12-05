#include <stdio.h>

int main() {
    float a;
    float b;
    float area;
    printf("ingresa base");
    scanf("%f",&a);
    printf("ingresa la altura ");
    scanf("%f",&b);
    area=(a * b)/2 ;
    printf("el resultado es %f\n",area);

    return 0;
}
