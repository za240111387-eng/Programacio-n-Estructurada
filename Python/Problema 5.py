import collections
import sys

# Ajuste para evitar errores de límite de recursión en árboles grandes.
sys.setrecursionlimit(2000) 

# --- Clase para la Mazmorra (Grafo/Árbol con Pesos) ---
class Dungeon:
    """Representa la mazmorra como un árbol de salas y pasillos con tiempos."""
    def __init__(self, n_salas):
        self.n = n_salas
        # Lista de adyacencia: {sala: [(vecino, tiempo), ...]}
        self.adj = collections.defaultdict(list)
        self.total_time_sum = 0 # Suma de todos los tiempos de pasillo (S)

    def agregar_pasillo(self, u, v, tiempo):
        """Añade una conexión bidireccional entre dos salas."""
        if u < 1 or u > self.n or v < 1 or v > self.n or tiempo <= 0:
            raise ValueError("Pasillo inválido: nodos fuera de rango (1 a N) o tiempo no positivo.")
            
        self.adj[u].append((v, tiempo))
        self.adj[v].append((u, tiempo))
        self.total_time_sum += tiempo

    def bfs_distancia(self, inicio):
        """
        Calcula el tiempo mínimo desde 'inicio' a todas las demás salas
        usando Breadth-First Search adaptado para pesos.
        """
        distancias = {i: float('inf') for i in range(1, self.n + 1)}
        
        # Cola de tuplas (sala, distancia_acumulada)
        cola = collections.deque([(inicio, 0)]) 
        distancias[inicio] = 0

        while cola:
            u, d = cola.popleft()
            
            for v, t in self.adj[u]:
                if distancias[v] == float('inf'):
                    distancias[v] = d + t
                    cola.append((v, d + t))
        return distancias


def resolver_escenario(dungeon, inicio, llave, trampa):
    """
    Calcula el tiempo mínimo para explorar todas las salas con las restricciones.
    """
    
    # Validación simple
    if not (1 <= inicio <= dungeon.n and 1 <= llave <= dungeon.n and 1 <= trampa <= dungeon.n):
        return "IMPOSSIBLE"
        
    # 1. Distancia mínima desde el Inicio (I) hasta la Trampa (T)
    dist_i = dungeon.bfs_distancia(inicio)
    t_i_t = dist_i.get(trampa, float('inf'))
    
    if t_i_t == float('inf'):
        return "IMPOSSIBLE"

    # 2. Fórmula de Recorrido de Árbol (mínimo tiempo para visitar todo)
    # T_min = 2 * (Suma Total de Tiempos) - Distancia(Inicio, Trampa)
    # Esta ruta garantiza visitar todas las salas y, por ende, la Llave,
    # antes de terminar efectivamente el recorrido en la Trampa.
    
    tiempo_minimo = 2 * dungeon.total_time_sum - t_i_t

    return int(tiempo_minimo) 


def dungeon_crawler_main():
    """Función principal para la interacción con el usuario y la ejecución."""
    
    try:
        print("--- Explorador de Mazmorras (Dungeon Crawler) ---")
        print("Ingrese n (salas) y q (consultas) separados por espacio (e.g., 5 2):")
        
        # Lectura de N y Q
        line = sys.stdin.readline().strip()
        if not line: return

        try:
            parts = line.split()
            if len(parts) != 2: raise ValueError
            n, q = map(int, parts)
        except ValueError:
            print("Error: n y q deben ser 2 números enteros separados por espacio.")
            return

        if n < 1:
            print("Error: n (salas) debe ser positivo.")
            return

        if n == 1:
            dungeon = Dungeon(1)
        else:
            dungeon = Dungeon(n)
        
            # --- Lectura de pasillos (n-1 aristas) ---
            print(f"\nIngrese {n - 1} pasillos en formato: u v tiempo (e.g., 1 2 5):")
            for i in range(n - 1):
                line = sys.stdin.readline().strip()
                if not line: 
                    print(f"Advertencia: Se esperaban {n-1} pasillos. Terminando la lectura.")
                    break 

                try:
                    parts = line.split()
                    if len(parts) != 3: raise ValueError
                    u, v, t = map(int, parts)
                    dungeon.agregar_pasillo(u, v, t)
                except ValueError:
                    print(f"Error en la línea del pasillo {i+1}. Formato incorrecto. Se esperaban 3 números enteros.")
                    return
                except Exception as e:
                    print(f"Error al agregar pasillo: {e}")
                    return
        
        print(f"\nTotal de tiempo de aristas (S): {dungeon.total_time_sum}")

        # --- Lectura y resolución de escenarios (consultas) ---
        resultados = []
        print(f"\nIngrese {q} escenarios en formato: inicio llave trampa (e.g., 1 3 5):")
        for i in range(q):
            print(f"Escenario {i+1}:", end=" ")
            line = sys.stdin.readline().strip()

            if not line: break 

            try:
                parts = line.split()
                if len(parts) != 3: raise ValueError
                inicio, llave, trampa = map(int, parts)

                if n == 1:
                    tiempo = 0 if inicio == 1 and llave == 1 and trampa == 1 else "IMPOSSIBLE"
                else:
                    tiempo = resolver_escenario(dungeon, inicio, llave, trampa)
                
                resultados.append(f"Escenario {i+1} (I:{inicio}, L:{llave}, T:{trampa}): {tiempo}")
            except ValueError:
                resultados.append(f"Escenario {i+1}: IMPOSSIBLE (Formato de escenario incorrecto. Se esperaban 3 números.)")
            except Exception as e:
                resultados.append(f"Escenario {i+1}: ERROR ({e})")

        # --- Mostrar Resultados ---
        print("\n--- RESULTADOS FINALES ---")
        for res in resultados:
            print(res)

    except Exception as e:
        print(f"\nOcurrió un error general de entrada: {e}")

if __name__ == "__main__":
    dungeon_crawler_main()
