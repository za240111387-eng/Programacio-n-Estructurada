#include <stdio.h>

int main() {
    float gastos[30], total = 0, promedio, temp;
    int i, j, dias[30];
    float gastoFinSemana = 0, gastoEntreSemana = 0;
    int contFinSemana = 0, contEntreSemana = 0;

    printf("ANALISIS DE GASTOS PERSONALES MENSUALES \n");

    for(i = 0; i < 30; i++) {
        printf("Ingrese el gasto del dia %d: $", i + 1);
        scanf("%f", &gastos[i]);
        total += gastos[i];
        dias[i] = i + 1;
    }


    promedio = total / 30.0;


    for(i = 0; i < 29; i++) {
        for(j = 0; j < 29 - i; j++) {
            if(gastos[j] > gastos[j + 1]) {
                temp = gastos[j];
                gastos[j] = gastos[j + 1];
                gastos[j + 1] = temp;


                int tempDia = dias[j];
                dias[j] = dias[j + 1];
                dias[j + 1] = tempDia;
            }
        }
    }


    printf("\nGasto total del mes: $%.2f\n", total);
    printf("Promedio diario: $%.2f\n", promedio);

    printf("\n 3 días con MENOR gasto \n");
    for(i = 0; i < 3; i++) {
        printf("Día %d: $%.2f\n", dias[i], gastos[i]);
    }

    printf("\n3 días con MAYOR gasto \n");
    for(i = 29; i > 26; i--) {
        printf("Día %d: $%.2f\n", dias[i], gastos[i]);
    }


    for(i = 0; i < 30; i++) {
        int diaSemana = (i + 1) % 7; // 1=lunes ... 6=sábado, 0=domingo
        if(diaSemana == 6 || diaSemana == 0) {
            gastoFinSemana += gastos[i];
            contFinSemana++;
        } else {
            gastoEntreSemana += gastos[i];
            contEntreSemana++;
        }
    }

    float promFinSemana = gastoFinSemana / contFinSemana;
    float promEntreSemana = gastoEntreSemana / contEntreSemana;

    printf("\nANALISIS DE PATRONES \n");
    printf("Promedio gasto entre semana: $%.2f\n", promEntreSemana);
    printf("Promedio gasto fines de semana: $%.2f\n", promFinSemana);

    if(promFinSemana > promEntreSemana)
        printf("Patrón detectado: Gastas más los fines de semana.\n");
    else if(promFinSemana < promEntreSemana)
        printf("Patrón detectado: Gastas más entre semana.\n");
    else
        printf("No hay diferencia significativa entre semana y fin de semana.\n");

    return 0;
}
