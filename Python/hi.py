import numpy as np

def densidad_electrones_libres():
    """
    Calcula la densidad de electrones libres para un metal.
    """
    # 1. Solicitar datos al usuario
    material = input("Ingresa el nombre del material (por ejemplo, 'Cobre'): ")
    try:
        densidad = float(input(f"Ingresa la densidad del {material} en g/cm³: "))
        masa_molar = float(input(f"Ingresa la masa molar del {material} en g/mol: "))
        electrones_valencia = int(input(f"Ingresa el número de electrones de valencia por átomo del {material}: "))
        temperatura = float(input("Ingresa la temperatura en Kelvin (K): ")) # La temperatura no afecta este cálculo
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    # 2. Constante de Avogadro en átomos/mol
    NA = 6.022e23
    
    # 3. Calcular la densidad atómica
    densidad_atomica = (densidad * NA) / masa_molar # átomos/cm³

    # 4. Calcular la densidad de electrones libres
    n1 = densidad_atomica * electrones_valencia # electrones/cm³

    # 5. Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Material: {material}")
    print(f"Temperatura: {temperatura} K")
    print(f"Densidad de electrones libres (n1): {n1:.2e} electrones/cm³")
    print("------------------")

# Llamar a la función para ejecutarla
if __name__ == "__main__":
    densidad_electrones_libres()