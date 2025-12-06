#include <stdio.h>

#define DEPARTAMENTOS 5   // Número de departamentos
#define DIAS 30           // Días del mes

int main() {
    float consumo[DEPARTAMENTOS][DIAS];
    float totalDepto[DEPARTAMENTOS] = {0};
    float totalDia[DIAS] = {0};
    float promedioDepto[DEPARTAMENTOS];
    float promedioDia[DIAS];
    float totalEdificio = 0, promedioGeneral = 0;
    int i, j;

    printf(" CONTROL DE CONSUMO DE AGUA EN EDIFICIO \n");

    // Entrada de datos
    for(i = 0; i < DEPARTAMENTOS; i++) {
        printf("\nDepartamento %d:\n", i + 1);
        for(j = 0; j < DIAS; j++) {
            printf("  Consumo del día %d (m3): ", j + 1);
            scanf("%f", &consumo[i][j]);
            totalDepto[i] += consumo[i][j];
            totalDia[j] += consumo[i][j];
            totalEdificio += consumo[i][j];
        }
    }


    for(i = 0; i < DEPARTAMENTOS; i++)
        promedioDepto[i] = totalDepto[i] / DIAS;

    for(j = 0; j < DIAS; j++)
        promedioDia[j] = totalDia[j] / DEPARTAMENTOS;

    promedioGeneral = totalEdificio / (DEPARTAMENTOS * DIAS);

    // Mostrar resultados
    printf("\n CONSUMO TOTAL Y PROMEDIO POR DEPARTAMENTO \n");
    for(i = 0; i < DEPARTAMENTOS; i++) {
        printf("Depto %d - Total: %.2f m3, Promedio diario: %.2f m3\n",
               i + 1, totalDepto[i], promedioDepto[i]);
    }

    printf("\n=== CONSUMO TOTAL Y PROMEDIO POR DÍA ===\n");
    for(j = 0; j < DIAS; j++) {
        printf("Día %2d - Total: %.2f m3, Promedio por depto: %.2f m3\n",
               j + 1, totalDia[j], promedioDia[j]);
    }


    printf("\n=== DETECCIÓN DE CONSUMOS ANÓMALOS ===\n");
    int hayAnomalos = 0;
    for(i = 0; i < DEPARTAMENTOS; i++) {
        if(promedioDepto[i] > 2 * promedioGeneral) {
            printf(" Departamento %d con consumo anómalo (%.2f m3/día)\n",
                   i + 1, promedioDepto[i]);
            hayAnomalos = 1;
        }
    }
    if(!hayAnomalos)
        printf("No se detectaron consumos anómalos.\n");


    printf("\n=== DETECCIÓN DE PICOS DE CONSUMO ===\n");
    float maxConsumoDia = 0;
    int diaPico = 0;
    for(j = 0; j < DIAS; j++) {
        if(totalDia[j] > maxConsumoDia) {
            maxConsumoDia = totalDia[j];
            diaPico = j;
        }
    }
    printf("Día con mayor consumo total: Día %d (%.2f m3)\n", diaPico + 1, maxConsumoDia);


    printf("\n=== TARIFA ESCALONADA (SIMULACIÓN DE PAGO) ===\n");
    printf("Tarifas:\n");
    printf(" - Hasta 15 m3: $10 por m3\n");
    printf(" - 16 a 30 m3: $12 por m3\n");
    printf(" - Más de 30 m3: $15 por m3\n\n");

    float pago[DEPARTAMENTOS];
    for(i = 0; i < DEPARTAMENTOS; i++) {
        if(totalDepto[i] <= 15)
            pago[i] = totalDepto[i] * 10;
        else if(totalDepto[i] <= 30)
            pago[i] = 15 * 10 + (totalDepto[i] - 15) * 12;
        else
            pago[i] = 15 * 10 + 15 * 12 + (totalDepto[i] - 30) * 15;

        printf("Depto %d - Consumo: %.2f m3 → Pago mensual: $%.2f\n",
               i + 1, totalDepto[i], pago[i]);
    }

    printf("\nPromedio general de consumo diario del edificio: %.2f m3\n", promedioGeneral);
    printf("Total mensual del edificio: %.2f m3\n", totalEdificio);

    return 0;
}
