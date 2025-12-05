#include <stdio.h>

#define ZONAS 5
#define CONTAMINANTES 3
#define HORAS 168 // 7 días * 24 horas

int main() {
    int z, c, h;
    float medicion[ZONAS][CONTAMINANTES][HORAS];
    float promedioZona[ZONAS][CONTAMINANTES] = {0};
    float maxZona[ZONAS][CONTAMINANTES] = {0};
    float promedioHora[HORAS][CONTAMINANTES] = {0};
    float maxHora[HORAS][CONTAMINANTES] = {0};
    float totalZona[ZONAS][CONTAMINANTES] = {0};
    float totalHora[HORAS][CONTAMINANTES] = {0};
    float sumaTotal = 0;

    printf("=== MONITOREO DE CALIDAD DEL AIRE ===\n");

    // Ingreso de datos
    for(z = 0; z < ZONAS; z++) {
        printf("\n--- Zona %d ---\n", z + 1);
        for(c = 0; c < CONTAMINANTES; c++) {
            printf(" Contaminante %d (ppm) durante %d horas:\n", c + 1, HORAS);
            for(h = 0; h < HORAS; h++) {
                printf("  Hora %d: ", h + 1);
                scanf("%f", &medicion[z][c][h]);
                totalZona[z][c] += medicion[z][c][h];
                totalHora[h][c] += medicion[z][c][h];
                sumaTotal += medicion[z][c][h];
                if(medicion[z][c][h] > maxZona[z][c])
                    maxZona[z][c] = medicion[z][c][h];
                if(medicion[z][c][h] > maxHora[h][c])
                    maxHora[h][c] = medicion[z][c][h];
            }
        }
    }

    // Calcular promedios por zona y contaminante
    for(z = 0; z < ZONAS; z++) {
        for(c = 0; c < CONTAMINANTES; c++) {
            promedioZona[z][c] = totalZona[z][c] / HORAS;
        }
    }

    // Calcular promedios por hora
    for(h = 0; h < HORAS; h++) {
        for(c = 0; c < CONTAMINANTES; c++) {
            promedioHora[h][c] = totalHora[h][c] / ZONAS;
        }
    }

    // Mostrar promedios y máximos por zona
    printf("\n=== PROMEDIO Y MÁXIMO POR ZONA ===\n");
    for(z = 0; z < ZONAS; z++) {
        printf("\nZona %d:\n", z + 1);
        for(c = 0; c < CONTAMINANTES; c++) {
            printf(" Contaminante %d - Promedio: %.2f, Máximo: %.2f\n", c + 1, promedioZona[z][c], maxZona[z][c]);
        }
    }

    // Identificar zonas y horas críticas
    printf("\n=== ZONAS Y HORAS CON NIVELES CRÍTICOS (superan 75 ppm) ===\n");
    for(z = 0; z < ZONAS; z++) {
        for(c = 0; c < CONTAMINANTES; c++) {
            for(h = 0; h < HORAS; h++) {
                if(medicion[z][c][h] > 75.0) {
                    printf("Zona %d - Contaminante %d - Hora %d: Nivel crítico (%.2f ppm)\n",
                           z + 1, c + 1, h + 1, medicion[z][c][h]);
                }
            }
        }
    }

    // Correlación simple entre contaminantes (suben juntos)
    printf("\n=== POSIBLES CORRELACIONES ENTRE CONTAMINANTES ===\n");
    for(h = 0; h < HORAS; h++) {
        int subida = 1;
        float base = promedioHora[h][0];
        for(c = 1; c < CONTAMINANTES; c++) {
            if(promedioHora[h][c] < base) {
                subida = 0;
                break;
            }
        }
        if(subida)
            printf("Hora %d: todos los contaminantes aumentaron juntos.\n", h + 1);
    }

    printf("\nAnálisis completado.\n");

    return 0;
}
