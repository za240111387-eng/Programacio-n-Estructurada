#include <stdio.h>

#define PISOS 3
#define HABITACIONES 10
#define DIAS 30

int main() {
    int piso, hab, dia;
    int ocupacion[PISOS][HABITACIONES][DIAS];
    float promPiso[PISOS] = {0}, promHab[PISOS][HABITACIONES] = {0}, promDia[DIAS] = {0};
    int totalOcupado = 0, totalPosibles = PISOS * HABITACIONES * DIAS;

    printf("=== GESTIÓN DE RESERVAS EN UN HOTEL ===\n");

    // Ingreso de datos (1 = ocupado, 0 = libre)
    for(piso = 0; piso < PISOS; piso++) {
        printf("\n--- Piso %d ---\n", piso + 1);
        for(hab = 0; hab < HABITACIONES; hab++) {
            printf("Habitación %d (1=ocupado, 0=libre) por %d días:\n", hab + 1, DIAS);
            for(dia = 0; dia < DIAS; dia++) {
                printf(" Día %d: ", dia + 1);
                scanf("%d", &ocupacion[piso][hab][dia]);
                // Validación de entrada
                if(ocupacion[piso][hab][dia] != 0 && ocupacion[piso][hab][dia] != 1) {
                    printf("  Valor inválido. Ingrese 0 o 1: ");
                    scanf("%d", &ocupacion[piso][hab][dia]);
                }
            }
        }
    }

    // Cálculo de promedios
    for(piso = 0; piso < PISOS; piso++) {
        for(hab = 0; hab < HABITACIONES; hab++) {
            int sumaHab = 0;
            for(dia = 0; dia < DIAS; dia++) {
                sumaHab += ocupacion[piso][hab][dia];
                promDia[dia] += ocupacion[piso][hab][dia];
                totalOcupado += ocupacion[piso][hab][dia];
            }
            promHab[piso][hab] = (float)sumaHab / DIAS;
            promPiso[piso] += sumaHab;
        }
        promPiso[piso] /= (HABITACIONES * DIAS);
    }

    // Calcular promedio por día
    for(dia = 0; dia < DIAS; dia++) {
        promDia[dia] /= (PISOS * HABITACIONES);
    }

    // Mostrar promedios
    printf("\n=== PROMEDIOS DE OCUPACIÓN ===\n");
    for(piso = 0; piso < PISOS; piso++) {
        printf("Piso %d - Ocupación promedio: %.2f\n", piso + 1, promPiso[piso]);
    }

    printf("\nPromedio por habitación (primer piso como ejemplo):\n");
    for(hab = 0; hab < HABITACIONES; hab++) {
        printf(" Habitación %d: %.2f\n", hab + 1, promHab[0][hab]);
    }

    printf("\nPromedio por día:\n");
    for(dia = 0; dia < DIAS; dia++) {
        printf(" Día %d: %.2f\n", dia + 1, promDia[dia]);
    }

    // Detectar habitaciones nunca o siempre ocupadas
    printf("\n=== HABITACIONES ESPECIALES ===\n");
    for(piso = 0; piso < PISOS; piso++) {
        for(hab = 0; hab < HABITACIONES; hab++) {
            int ocupados = 0;
            for(dia = 0; dia < DIAS; dia++) {
                ocupados += ocupacion[piso][hab][dia];
            }
            if(ocupados == 0)
                printf("Piso %d Habitación %d: NUNCA ocupada.\n", piso + 1, hab + 1);
            else if(ocupados == DIAS)
                printf("Piso %d Habitación %d: SIEMPRE ocupada.\n", piso + 1, hab + 1);
        }
    }

    // Días con máxima y mínima ocupación
    int diaMax = 0, diaMin = 0;
    float maxOcup = promDia[0], minOcup = promDia[0];
    for(dia = 1; dia < DIAS; dia++) {
        if(promDia[dia] > maxOcup) {
            maxOcup = promDia[dia];
            diaMax = dia;
        }
        if(promDia[dia] < minOcup) {
            minOcup = promDia[dia];
            diaMin = dia;
        }
    }

    printf("\n=== DÍAS DE OCUPACIÓN MÁXIMA Y MÍNIMA ===\n");
    printf("Día con mayor ocupación: Día %d (%.2f)\n", diaMax + 1, maxOcup);
    printf("Día con menor ocupación: Día %d (%.2f)\n", diaMin + 1, minOcup);

    printf("\nOcupación total del mes: %.2f%%\n", (float)totalOcupado / totalPosibles * 100);

    return 0;
}
