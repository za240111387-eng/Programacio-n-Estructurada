#include <stdio.h>

#define SALONES 5
#define HORAS 8

int main() {
    int i, j, h;
    int disponibilidad[SALONES][HORAS];
    int ocupadasPorHora[HORAS] = {0};
    int salonSiempreOcupado = -1, salonNuncaUsado = -1;
    int consecutivas, horaInicio, horasRequeridas;
    int maxDemanda = 0, horaMayorDemanda = 0;

    printf("PLANIFICACIÓN DE HORARIOS ESCOLARES \n");


    for(i = 0; i < SALONES; i++) {
        printf("\n--- Salon %d ---\n", i + 1);
        for(j = 0; j < HORAS; j++) {
            printf("Hora %d (0=Libre, 1=Ocupado): ", j + 1);
            scanf("%d", &disponibilidad[i][j]);
        }
    }


    for(j = 0; j < HORAS; j++) {
        for(i = 0; i < SALONES; i++) {
            if(disponibilidad[i][j] == 1)
                ocupadasPorHora[j]++;
        }
        if(ocupadasPorHora[j] > maxDemanda) {
            maxDemanda = ocupadasPorHora[j];
            horaMayorDemanda = j;
        }
    }

    printf("\n=== DEMANDA DE SALONES POR HORA ===\n");
    for(j = 0; j < HORAS; j++) {
        printf("Hora %d: %d salones ocupados\n", j + 1, ocupadasPorHora[j]);
    }

    printf("\nHora con mayor demanda: %d (con %d salones ocupados)\n",
           horaMayorDemanda + 1, maxDemanda);


    for(i = 0; i < SALONES; i++) {
        int ocupadas = 0, libres = 0;
        for(j = 0; j < HORAS; j++) {
            if(disponibilidad[i][j] == 1)
                ocupadas++;
            else
                libres++;
        }
        if(ocupadas == HORAS)
            salonSiempreOcupado = i;
        if(libres == HORAS)
            salonNuncaUsado = i;
    }

    if(salonSiempreOcupado != -1)
        printf("\nEl salón %d está SIEMPRE ocupado.\n", salonSiempreOcupado + 1);
    else
        printf("\nNo hay salones siempre ocupados.\n");

    if(salonNuncaUsado != -1)
        printf("El salón %d NUNCA se usa.\n", salonNuncaUsado + 1);
    else
        printf("No hay salones sin uso.\n");

    // Buscar bloque de horas consecutivas libres para evento
    printf("\n BUSCAR HORAS LIBRES PARA EVENTO \n");
    printf("Ingrese el número de horas consecutivas requeridas: ");
    scanf("%d", &horasRequeridas);

    int encontrado = 0;
    for(i = 0; i < SALONES && !encontrado; i++) {
        consecutivas = 0;
        for(j = 0; j < HORAS; j++) {
            if(disponibilidad[i][j] == 0)
                consecutivas++;
            else
                consecutivas = 0;

            if(consecutivas == horasRequeridas) {
                horaInicio = j - horasRequeridas + 1;
                printf("Salón %d tiene %d horas libres consecutivas desde la hora %d hasta %d.\n",
                       i + 1, horasRequeridas, horaInicio + 1, j + 1);
                encontrado = 1;
                break;
            }
        }
    }

    if(!encontrado)
        printf("No se encontró un bloque libre de %d horas consecutivas.\n", horasRequeridas);

    // Reto adicional: Simular reasignación para optimizar uso
    printf("\n REASIGNACIÓN DE HORARIOS (SIMULACIÓN) \n");
    for(j = 0; j < HORAS; j++) {
        int ocupados = 0;
        for(i = 0; i < SALONES; i++)
            if(disponibilidad[i][j] == 1) ocupados++;

        // Si hay menos del 50% de salones ocupados, asignar más grupos
        if(ocupados < SALONES / 2) {
            for(i = 0; i < SALONES && ocupados < SALONES / 2 + 1; i++) {
                if(disponibilidad[i][j] == 0) {
                    disponibilidad[i][j] = 1; // asignamos un nuevo grupo
                    ocupados++;
                }
            }
        }
    }

    printf("Se ha simulado una reasignación para mejorar el uso de los salones.\n");

    printf("\n NUEVA MATRIZ DE DISPONIBILIDAD (1=Ocupado, 0=Libre) \n");
    for(i = 0; i < SALONES; i++) {
        printf("Salón %d: ", i + 1);
        for(j = 0; j < HORAS; j++)
            printf("%d ", disponibilidad[i][j]);
        printf("\n");
    }

    return 0;
}
