int main() {
    float corriente, voltaje;

    // Entrada de datos
    printf("Ingrese la corriente medida (A): ");
    scanf("%f", &corriente);

    printf("Ingrese el voltaje medido (V): ");
    scanf("%f", &voltaje);

    // Condición compuesta
    if (corriente > 3 && voltaje < 1) {
        printf("Alarma de cortocircuito ACTIVADA.\n");
    } else {
        printf("Sistema en monitoreo continuo...\n");
    }

    return 0;
}
