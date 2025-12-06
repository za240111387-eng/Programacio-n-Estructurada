#include <stdio.h>

int main() {
    float voltaje;

    printf("Ingrese el voltaje de la bateria (V): ");
    scanf("%f", &voltaje);

    if (voltaje < 11) {
        printf("Bateria baja.\n");
    } else if (voltaje <= 12.6) {
        printf("Bateria normal.\n");
    } else {
        printf("Sobrecarga.\n");
    }

    return 0;
}
