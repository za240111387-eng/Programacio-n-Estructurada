import numpy as np

# Constante de Boltzmann en eV/K
kB = 8.617e-5

def calcular_densidad_electrones(material: str, temperatura: float):
    """
    Calcula la densidad de electrones libres en electrones/cm^3 para un material dado a una temperatura específica.

    Args:
        material (str): El nombre del material (ej. 'silicio', 'cobre', 'germanio').
        temperatura (float): La temperatura en Kelvin.

    Returns:
        float: La densidad de electrones libres en electrones/cm^3.
    """
    material = material.lower()
    
    if material == 'silicio' or material == 'germanio':
        # Datos para semiconductores intrínsecos a 300 K
        if material == 'silicio':
            Eg = 1.12 # eV (bandgap)
            Nc = 2.8e19 # 1/cm^3
            Nv = 1.04e19 # 1/cm^3
        else: # germanio
            Eg = 0.66 # eV
            Nc = 1.04e19 # 1/cm^3
            Nv = 6.0e18 # 1/cm^3

        # Para un semiconductor intrínseco (no dopado) la densidad de electrones (n)
        # es igual a la densidad de huecos (p), y se puede calcular como n_i (densidad intrínseca)
        # n_i = sqrt(Nc * Nv) * exp(-Eg / (2 * kB * T))
        n = np.sqrt(Nc * Nv) * np.exp(-Eg / (2 * kB * temperatura))
        return n
    
    elif material == 'cobre':
        # Para metales, la densidad de electrones es independiente de la temperatura
        # Datos para Cobre:
        # Densidad (rho) = 8.96 g/cm^3
        # Peso atómico (AW) = 63.546 g/mol
        # Electrones de valencia = 1 (para Cu)
        
        rho = 8.96 # g/cm^3
        AW = 63.546 # g/mol
        valencia = 1
        NA = 6.022e23 # Avogadro's number
        
        # n = (rho * NA * valencia) / AW
        n = (rho * NA * valencia) / AW
        return n
        
    else:
        print(f"Material '{material}' no reconocido. Por favor, use 'silicio', 'germanio' o 'cobre'.")
        return None

# Ejemplos de uso
print(f"Densidad de electrones en Silicio a 300 K: {calcular_densidad_electrones('silicio', 300):.2e} electrones/cm^3")
print(f"Densidad de electrones en Cobre: {calcular_densidad_electrones('cobre', 300):.2e} electrones/cm^3")
print(f"Densidad de electrones en Germanio a 400 K: {calcular_densidad_electrones('germanio', 400):.2e} electrones/cm^3")