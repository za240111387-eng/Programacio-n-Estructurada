import sys
import collections

# Aumentamos el límite de recursión por si el cristal es grande
sys.setrecursionlimit(2000)

# Variables globales para almacenar las soluciones Mínima y Máxima
# Se usan valores fuera del rango posible para asegurar que la primera solución se guarde
solucion_minima = None
max_moleculas_minima = float('inf') 
solucion_maxima = None
min_moleculas_maxima = float('-inf') 

def imprimir_grilla(grilla, dx, dy):
    """Convierte la lista plana de la grilla a una cadena de caracteres para imprimir."""
    if grilla is None:
        return "No encontrada."
    
    output = ""
    for i in range(dy):
        # Mapeo de índice plano a coordenadas (y, x)
        fila = grilla[i * dx : (i + 1) * dx]
        output += "".join(['*' if c == 1 else 'o' for c in fila]) + "\n"
    return output

def verificar_consistencia(grilla, vientos_y_limites, dx, dy):
    """
    Verifica si la grilla dada es consistente con todas las observaciones de viento.
    Retorna True si es consistente, False en caso contrario.
    """
    for obs in vientos_y_limites:
        wx, wy = obs['viento']
        for x, y in obs['limites']:
            # Coordenadas de la celda vecina en la dirección del viento
            nx, ny = x + wx, y + wy
            
            # Condición 1: Existe molécula en el punto de límite (x, y)
            idx = y * dx + x
            if not (0 <= x < dx and 0 <= y < dy and grilla[idx] == 1):
                return False # Falla la primera condición
            
            # Condición 2: No existe molécula en el punto vecino (nx, ny)
            if 0 <= nx < dx and 0 <= ny < dy:
                n_idx = ny * dx + nx
                if grilla[n_idx] == 1:
                    return False # Falla la segunda condición
            # Si el punto vecino está fuera de los límites, la condición 2 se satisface.
    return True

def buscar_soluciones(index, grilla_actual, conteo_moleculas, vientos_y_limites, dx, dy):
    """
    Busca configuraciones consistentes de forma recursiva (backtracking/DFS).
    """
    global solucion_minima, max_moleculas_minima, solucion_maxima, min_moleculas_maxima

    if index == dx * dy:
        # Caso base: La grilla está completa.
        if verificar_consistencia(grilla_actual, vientos_y_limites, dx, dy):
            # Guardar la solución Mínima
            if conteo_moleculas < max_moleculas_minima:
                max_moleculas_minima = conteo_moleculas
                solucion_minima = list(grilla_actual) 
            
            # Guardar la solución Máxima
            if conteo_moleculas > min_moleculas_maxima:
                min_moleculas_maxima = conteo_moleculas
                solucion_maxima = list(grilla_actual) 
        return

    # --- PODA (Pruning) ---
    restantes = dx * dy - index
    # Poda para la solución MÁXIMA: si el máximo posible no supera la MAX actual
    if solucion_maxima and (conteo_moleculas + restantes) <= min_moleculas_maxima:
        return 

    # --- RECURSIVIDAD ---

    # 1. Prueba SIN molécula (0)
    grilla_actual[index] = 0
    buscar_soluciones(index + 1, grilla_actual, conteo_moleculas, vientos_y_limites, dx, dy)

    # 2. Prueba CON molécula (1) - Aplicando restricción local
    y = index // dx
    x = index % dx
    
    puede_poner_molecula = True
    
    # Verificación local: La celda actual (x, y) no puede ser el punto vacío
    # de ninguna observación de límite existente.
    for obs in vientos_y_limites:
        wx, wy = obs['viento']
        for lx, ly in obs['limites']:
            # La celda vecina que NO debe tener molécula es (lx + wx, ly + wy)
            if x == lx + wx and y == ly + wy:
                puede_poner_molecula = False
                break
        if not puede_poner_molecula:
            break

    if puede_poner_molecula:
        grilla_actual[index] = 1
        buscar_soluciones(index + 1, grilla_actual, conteo_moleculas + 1, vientos_y_limites, dx, dy)
        
    # Backtrack (aunque la recursión maneja la copia en este caso, se restablece para claridad)
    grilla_actual[index] = 0


def resolver_viento_en_cristal():
    """Función principal para gestionar la entrada y ejecución."""
    
    print("--- PROBLEMA: VIENTO EN CRISTAL (CRYSTAL CROSSWIND) ---")

    # --- ENTRADA DE DATOS ---
    try:
        dx = int(input("Introduce la dimensión máxima DX (columnas): "))
        dy = int(input("Introduce la dimensión máxima DY (filas): "))
        k = int(input("Introduce el número de vientos (K): "))
        if dx <= 0 or dy <= 0 or k < 0:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números enteros positivos.")
        return

    vientos_y_limites = []
    print("\nIntroduce los datos para cada viento (formato: wx, wy, x1, y1, x2, y2, ...):")
    
    for i in range(k):
        while True:
            try:
                linea = input(f"Viento {i+1} (wx, wy, límites separados por coma y sin espacios): ")
                
                # Reemplazamos los espacios para manejar entradas como '1, 1, 3, 3'
                linea = linea.replace(' ', '')
                if not linea: continue
                
                partes = [int(p) for p in linea.split(',')]
                
                if len(partes) < 2 or (len(partes) - 2) % 2 != 0:
                    raise ValueError("Número incorrecto de componentes (Se esperan wx, wy y pares de límites x,y).")
                
                wx, wy = partes[0], partes[1]
                
                limites = []
                for j in range(2, len(partes), 2):
                    x, y = partes[j], partes[j+1]
                    # Solo aceptamos límites dentro del cristal para el procesamiento
                    if 0 <= x < dx and 0 <= y < dy:
                         limites.append((x, y))
                    else:
                         print(f"Advertencia: El límite ({x}, {y}) está fuera del rango [0,{dx-1}]x[0,{dy-1}] y fue omitido.")
                
                if not limites and len(partes) > 2:
                    print("Advertencia: Todos los límites observados estaban fuera de rango. Viento omitido.")
                    continue
                    
                vientos_y_limites.append({
                    'viento': (wx, wy),
                    'limites': limites
                })
                break
            except ValueError as e:
                print(f"Formato incorrecto. Ejemplo: 1,1,3,3,5,5. Error: {e}")

    # --- EJECUCIÓN DEL ALGORITMO ---
    
    grilla_inicial = [0] * (dx * dy)
    
    print("\nIniciando búsqueda de configuraciones...")
    buscar_soluciones(0, grilla_inicial, 0, vientos_y_limites, dx, dy)
    
    # --- RESULTADOS ---

    print("\n" + "=" * 40)
    print("        RESULTADOS FINALES")
    print("=" * 40)

    # 1. Configuración Mínima
    print(f"## 1. Configuración con MÍNIMO de moléculas ({max_moleculas_minima if solucion_minima else 'N/A'}):")
    print("-" * 40)
    print(imprimir_grilla(solucion_minima, dx, dy))
    print("-" * 40)

    # 2. Configuración Máxima
    print(f"## 2. Configuración con MÁXIMO de moléculas ({min_moleculas_maxima if solucion_maxima else 'N/A'}):")
    print("-" * 40)
    print(imprimir_grilla(solucion_maxima, dx, dy))
    print("-" * 40)

    if solucion_minima is None and solucion_maxima is None:
        print("¡ADVERTENCIA! No se encontró ninguna configuración que satisfaga todas las restricciones.")

# Ejecución del programa
if __name__ == "__main__":
    resolver_viento_en_cristal()