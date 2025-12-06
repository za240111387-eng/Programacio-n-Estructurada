#include <stdio.h>

int main() {
    float temperatura;

    printf("Ingrese la temperatura en °C: ");
    scanf("%f", &temperatura);

    if (temperatura < 50) {
        printf("Frio\n");
    } else if (temperatura >= 50 && temperatura <= 150) {
        printf("Temperatura Normal\n");
    } else {
        printf("Alerta: Caliente\n");
    }

    return 0;
}
