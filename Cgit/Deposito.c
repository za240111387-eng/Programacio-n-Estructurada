#include <stdio.h>

int main() {
    float nivel;

    printf("Ingrese el nivel del deposito (en %%): ");
    scanf("%f", &nivel);

    if (nivel < 10) {
        printf("Deposito vacio.\n");
    } else if (nivel <= 90) {
        printf("Niveles normales.\n");
    } else {
        printf("Posible desbordamiento.\n");
    }

    return 0;
}
