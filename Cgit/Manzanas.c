#include <stdio.h>

int main() {
    int venta_manzanas[7]={15, 20, 13, 22,18,25,17};
    int total=0, i;
    for (i=0; i<7; i++){
        total += venta_manzanas[i];
    }
    printf("total vendido: %d\n", total);

    return 0;
}
