#include <stdio.h>

int main() {
    float a;
    float fahrenheit;

    printf("ingresa temperatura en celcius ");
    scanf("%f",&a);

    fahrenheit = a * 9/5+32 ;
    printf("el total es %f\n",fahrenheit);
    return 0;
}
