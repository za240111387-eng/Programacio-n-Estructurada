#include <stdio.h>

int main() {
    int lux;  // variable para almacenar la lectura del sensor

    printf("Ingrese la lectura del sensor de luz (en lux): ");
    scanf("%d", &lux);

    if (lux < 300) {
        printf("La lámpara debe ENCENDERSE.\n");
    } else {
        printf("La lámpara debe APAGARSE.\n");
    }

    return 0;
}
