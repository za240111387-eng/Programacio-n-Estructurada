#include <stdio.h>

int main() {
    float frecuencia;

    printf("Ingrese la frecuencia (Hz): ");
    scanf("%f", &frecuencia);

    if (frecuencia < 20) {
        printf("Sub-sonido.\n");
    } else if (frecuencia <= 20000) {
        printf("Sonido.\n");
    } else {
        printf("Ultrasonido.\n");
    }

    return 0;
}
