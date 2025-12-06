import sys

def resolver_mosaico():
    # --- 1. Lectura de Datos ---
    # Nota: Esta función asume que ingresas los datos línea por línea.
    # Puedes ajustar los inputs según cómo te den los datos (archivo o consola).
    
    print("Introduce las dimensiones del MOTIVO (filas columnas):")
    try:
        linea1 = sys.stdin.readline().split()
        if not linea1: return # Fin de entrada
        R_motivo, C_motivo = map(int, linea1)
    except ValueError:
        print("Error en formato de dimensiones.")
        return

    print("Introduce la matriz del MOTIVO:")
    motivo = []
    for _ in range(R_motivo):
        motivo.append(list(map(int, sys.stdin.readline().split())))

    print("Introduce las dimensiones del MOSAICO (filas columnas):")
    R_mosaico, C_mosaico = map(int, sys.stdin.readline().split())

    print("Introduce la matriz del MOSAICO:")
    mosaico = []
    for _ in range(R_mosaico):
        mosaico.append(list(map(int, sys.stdin.readline().split())))

    # --- 2. Pre-procesamiento del Motivo (Optimización) ---
    # Guardamos solo las posiciones que tienen color (valor > 0)
    # Formato: (fila_relativa, col_relativa, valor)
    puntos_a_verificar = []
    for r in range(R_motivo):
        for c in range(C_motivo):
            if motivo[r][c] != 0:
                puntos_a_verificar.append((r, c, motivo[r][c]))

    # --- 3. Búsqueda (Sliding Window) ---
    coincidencias = []

    # El motivo solo puede moverse hasta donde quepa dentro del mosaico
    limite_filas = R_mosaico - R_motivo + 1
    limite_cols = C_mosaico - C_motivo + 1

    for r in range(limite_filas):
        for c in range(limite_cols):
            match = True
            
            # Verificamos solo los puntos importantes del motivo
            for pr, pc, valor in puntos_a_verificar:
                # Coordenada absoluta en el mosaico
                mosaico_r = r + pr
                mosaico_c = c + pc
                
                if mosaico[mosaico_r][mosaico_c] != valor:
                    match = False
                    break # Si uno falla, pasamos a la siguiente posición
            
            if match:
                # Guardamos la posición (r+1, c+1) para usar base-1 como es común en estos problemas
                # Si tu problema requiere base-0, quita los "+ 1"
                coincidencias.append((r + 1, c + 1))

    # --- 4. Salida de Resultados ---
    print("\n--- RESULTADOS ---")
    print(f"Número de coincidencias: {len(coincidencias)}")
    print("Lista de posiciones (fila, columna):")
    for pos in coincidencias:
        print(f"{pos[0]}, {pos[1]}")

if __name__ == "__main__":
    resolver_mosaico()