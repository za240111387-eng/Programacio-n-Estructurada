#include <stdio.h>

int main() {
    int n, i, j, temp;
    float suma = 0, promedio, mediana;

    printf("GESTIÓN DE PUNTUACIONES EN TORNEO \n");
    printf("Ingrese el número de jugadores: ");
    scanf("%d", &n);

    float puntajes[n];


    for(i = 0; i < n; i++) {
        printf("Puntuación del jugador %d: ", i + 1);
        scanf("%f", &puntajes[i]);
        suma += puntajes[i];
    }


    promedio = suma / n;


    for(i = 0; i < n - 1; i++) {
        for(j = 0; j < n - i - 1; j++) {
            if(puntajes[j] < puntajes[j + 1]) {
                temp = puntajes[j];
                puntajes[j] = puntajes[j + 1];
                puntajes[j + 1] = temp;
            }
        }
    }


    if(n % 2 == 0)
        mediana = (puntajes[n/2 - 1] + puntajes[n/2]) / 2.0;
    else
        mediana = puntajes[n/2];

    printf("\nPuntuación más alta: %.2f\n", puntajes[0]);
    printf("Puntuación más baja: %.2f\n", puntajes[n - 1]);
    printf("Mediana de puntuaciones: %.2f\n", mediana);
    printf("Promedio general: %.2f\n", promedio);


    int arribaProm = 0;
    for(i = 0; i < n; i++) {
        if(puntajes[i] > promedio)
            arribaProm++;
    }
    printf("\nJugadores por encima del promedio: %d\n", arribaProm);

    //
    printf("\n=== Análisis de empates en el podio ===\n");
    int hayEmpate = 0;
    for(i = 0; i < 2; i++) {
        for(j = i + 1; j < 3 && j < n; j++) {
            if(puntajes[i] == puntajes[j]) {
                printf("Empate detectado entre lugares %d y %d (%.2f puntos)\n", i + 1, j + 1, puntajes[i]);
                hayEmpate = 1;
            }
        }
    }
    if(!hayEmpate)
        printf("No hay empates en los primeros 3 lugares.\n");

    return 0;
}
