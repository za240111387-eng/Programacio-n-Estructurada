#include <stdio.h>

int main() {
    int i, j;
    float ventas[7][7];  // 7 productos x 7 días
    float totalProducto[7] = {0}, totalDia[7] = {0};
    float mayorVentaProducto = 0, mayorVentaDia = 0;
    int prodMasVendido = 0, diaMasVenta = 0;
    int sinVentas, haySinVentas = 0;

    printf(" CONTROL DE INVENTARIO - TIENDA DE ABARROTES \n");

    // Entrada de datos
    for(i = 0; i < 7; i++) {
        printf("\nProducto %d:\n", i + 1);
        for(j = 0; j < 7; j++) {
            printf("  Ventas del día %d: ", j + 1);
            scanf("%f", &ventas[i][j]);
        }
    }


    for(i = 0; i < 7; i++) {
        for(j = 0; j < 7; j++) {
            totalProducto[i] += ventas[i][j];
            totalDia[j] += ventas[i][j];
        }
    }


    printf("\n TOTAL VENDIDO POR PRODUCTO \n");
    for(i = 0; i < 7; i++) {
        printf("Producto %d: %.2f unidades vendidas\n", i + 1, totalProducto[i]);
        if(totalProducto[i] > mayorVentaProducto) {
            mayorVentaProducto = totalProducto[i];
            prodMasVendido = i;
        }
    }


    printf("\nTOTAL VENDIDO POR DÍA \n");
    for(j = 0; j < 7; j++) {
        printf("Día %d: %.2f unidades vendidas\n", j + 1, totalDia[j]);
        if(totalDia[j] > mayorVentaDia) {
            mayorVentaDia = totalDia[j];
            diaMasVenta = j;
        }
    }


    printf("\n ANÁLISIS DE RESULTADOS \n");
    printf("Producto más vendido de la semana: Producto %d (%.2f unidades)\n",
           prodMasVendido + 1, mayorVentaProducto);
    printf("Día con mayor venta total: Día %d (%.2f unidades)\n",
           diaMasVenta + 1, mayorVentaDia);

    // Detectar productos con días sin venta
    printf("\nPRODUCTOS SIN VENTAS ALGÚN DÍA \n");
    for(i = 0; i < 7; i++) {
        sinVentas = 0;
        for(j = 0; j < 7; j++) {
            if(ventas[i][j] == 0) {
                sinVentas = 1;
                break;
            }
        }
        if(sinVentas) {
            printf("El producto %d tuvo al menos un día sin ventas.\n", i + 1);
            haySinVentas = 1;
        }
    }

    if(!haySinVentas) {
        printf("Todos los productos se vendieron al menos una vez cada día.\n");
    }

    return 0;
}
