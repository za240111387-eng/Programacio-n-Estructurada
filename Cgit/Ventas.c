#include <stdio.h>

#define VENDEDORES 5
#define DIAS 7


void mostrarVentasTotalesPorDia(float total_dia[]);

int main() {
    float ventas[VENDEDORES][DIAS];
    float total_vendedor[VENDEDORES] = {0};
    float total_dia[DIAS] = {0};
    float promedio_vendedor[VENDEDORES];
    int i, j, dia_mayor = 0;
    float mayor_venta = 0;

    // Entrada de datos
    printf("=== REGISTRO DE VENTAS SEMANALES ===\n");
    for (i = 0; i < VENDEDORES; i++) {
        printf("\nVendedor %d:\n", i + 1);
        for (j = 0; j < DIAS; j++) {
            printf("  Día %d (venta en $): ", j + 1);
            scanf("%f", &ventas[i][j]);
            total_vendedor[i] += ventas[i][j];
            total_dia[j] += ventas[i][j];
        }
    }


    for (i = 0; i < VENDEDORES; i++) {
        promedio_vendedor[i] = total_vendedor[i] / DIAS;
    }

    // Día con mayores ventas totales
    for (j = 0; j < DIAS; j++) {
        if (total_dia[j] > mayor_venta) {
            mayor_venta = total_dia[j];
            dia_mayor = j;
        }
    }


    printf("\n===========================================\n");
    printf("   RESULTADOS DE DESEMPEÑO SEMANAL\n");
    printf("===========================================\n");

    for (i = 0; i < VENDEDORES; i++) {
        printf("Vendedor %d:\n", i + 1);
        printf("  Total vendido: $%.2f\n", total_vendedor[i]);
        printf("  Promedio semanal: $%.2f\n", promedio_vendedor[i]);
        printf("-------------------------------------------\n");
    }

    printf("\nDía con mayores ventas totales: Día %d\n", dia_mayor + 1);
    printf("Ventas totales ese día: $%.2f\n", mayor_venta);
    printf("===========================================\n");


    mostrarVentasTotalesPorDia(total_dia);

    return 0;
}

a
void mostrarVentasTotalesPorDia(float total_dia[]) {
    int j;
    printf("\n=== VENTAS TOTALES DE LA TIENDA POR DÍA ===\n");
    for (j = 0; j < DIAS; j++) {
        printf("Día %d: $%.2f\n", j + 1, total_dia[j]);
    }
    printf("===========================================\n");
}
