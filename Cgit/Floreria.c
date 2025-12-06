#include <stdio.h>

int main() {
    int n, i, j, temp, contador;
    float total = 0;

    printf("OPTIMIZACIÓN DE RUTAS DE ENTREGA \n");
    printf("Ingrese el número de pedidos del día: ");
    scanf("%d", &n);

    float distancias[n];


    for(i = 0; i < n; i++) {
        printf("Distancia del pedido %d (km): ", i + 1);
        scanf("%f", &distancias[i]);
    }


    for(i = 0; i < n - 1; i++) {
        for(j = 0; j < n - i - 1; j++) {
            if(distancias[j] > distancias[j + 1]) {
               temp = distancias[j];
                distancias[j] = distancias[j + 1];
                distancias[j + 1] = temp;
            }
        }
    }


    printf("\nDistancias ordenadas (ruta optimizada):\n");
    for(i = 0; i < n; i++) {
        printf("%.2f km  ", distancias[i]);
        total += distancias[i];
    }


    printf("\n\nDistancia total recorrida: %.2f km\n", total);


    printf("\nDistancias repetidas:\n");
    int hayRepetidas = 0;
    for(i = 0; i < n; i++) {
        contador = 1;
        for(j = i + 1; j < n; j++) {
            if(distancias[i] == distancias[j]) {
                contador++;
            } else {
                break;
            }
        }
        if(contador > 1) {
            printf("La distancia %.2f km se repite %d veces\n", distancias[i], contador);
            hayRepetidas = 1;
            i += contador - 1;
        }
    }

    if(!hayRepetidas) {
        printf("No hay distancias repetidas.\n");
    }

    return 0;
}
