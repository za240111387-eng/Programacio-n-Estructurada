#include <stdio.h>

int main() {
    int selector;

    printf("Ingrese la posición del selector (1, 2, 3 o 4): ");
    scanf("%d", &selector);

    switch (selector) {
        case 1:
            printf("Entrada 1 seleccionada.\n");
            break;
        case 2:
            printf("Entrada 2 seleccionada.\n");
            break;
        case 3:
            printf("Entrada 3 seleccionada.\n");
            break;
        case 4:
            printf("Entrada 4 seleccionada.\n");
            break;
        default:
            printf("Opción inválida.\n");
    }

    return 0;
}
