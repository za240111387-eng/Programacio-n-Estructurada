import sys
import collections

sys.setrecursionlimit(4000)

class NodoSplit:
    """Nodo que divide la secuencia de entrada: impares a Salida 1, pares a Salida 2."""
    def __init__(self, id_nodo, salidas):
        self.id = id_nodo
        # salidas es un diccionario {indice_salida: id_nodo_siguiente}
        self.salidas = salidas 

class NodoMerge:
    """Nodo que fusiona dos secuencias de entrada, alternando (E1, E2, E1, E2...)."""
    def __init__(self, id_nodo, entradas):
        self.id = id_nodo
        # entradas es una lista [id_nodo_entrada_1, id_nodo_entrada_2]
        self.entradas = entradas 

class SplitstreamNetwork:
    """
    Gestiona la red acíclica de procesamiento.
    Usa memoización para optimizar las consultas de indexación inversa.
    """
    def __init__(self, m_global):
        self.nodes = {}  
        self.m_global = m_global
        # Mapa de memoización
        self.origen_map = {} 

    def agregar_split(self, id_nodo, salidas):
        self.nodes[id_nodo] = NodoSplit(id_nodo, salidas)

    def agregar_merge(self, id_nodo, entradas):
        self.nodes[id_nodo] = NodoMerge(id_nodo, entradas)

    def calcular_origen_global(self, id_nodo, k, entrada_del_split=None):
        """
        Calcula recursivamente qué posición de la secuencia global (1, 2, 3...) 
        alimenta la posición 'k' en el flujo que sale de 'id_nodo'.
        """
        if k <= 0:
            return None
        
        

        # 1. Memoización
        if (id_nodo, k) in self.origen_map:
            return self.origen_map[(id_nodo, k)]

        nodo = self.nodes.get(id_nodo)
        resultado = None

        if nodo is None:

            return k

        # A. Procesar Nodo MERGE 
        if isinstance(nodo, NodoMerge):
            
            # 1. Determinar de qué entrada viene (E1 o E2) y con qué índice (k_origen)
            if k % 2 != 0:

                k_origen = (k + 1) // 2
                nodo_origen_id = nodo.entradas[0] 
            else:

                k_origen = k // 2
                nodo_origen_id = nodo.entradas[1] 

            # 2. Recurrir al nodo anterior
            resultado = self.calcular_origen_global(nodo_origen_id, k_origen)

        # B. Procesar Nodo SPLIT 
        elif isinstance(nodo, NodoSplit):
            resultado = k 


        # 3. Guardar y Retornar
        self.origen_map[(id_nodo, k)] = resultado
        return resultado


def resolver_splitstream():
    """Función principal para leer la entrada y ejecutar las consultas."""
    
    print("--- PROCESAMIENTO DE SECUENCIAS - SPLITSTREAM ---")
    
    try:
        # Lectura de Parámetros 
        m = int(input("Longitud de la secuencia global (m): "))
        n = int(input("Número de nodos (n): "))
        q = int(input("Número de consultas (q): "))
        
        if m <= 0 or n <= 0 or q <= 0:
            print("Las longitudes y cantidades deben ser positivas.")
            return

        network = SplitstreamNetwork(m)
        
        # Lectura de Nodos 
        print("\nDescripción de los nodos (tipo y conexiones):")
        print("Formato Split (salida 1, salida 2): S <id> <salida1> <salida2>")
        print("Formato Merge (entrada 1, entrada 2): M <id> <entrada1> <entrada2>")
        print("Nota: Use 0 para la entrada/salida global (periferia).")

        for _ in range(n):
            linea = input().split()
            if not linea: continue
                
            tipo = linea[0].upper()
            id_nodo = int(linea[1])
            
            if tipo == 'S':
                if len(linea) != 4: raise ValueError("Split requiere 4 valores.")
                salidas = {1: int(linea[2]), 2: int(linea[3])}
                network.agregar_split(id_nodo, salidas)
            elif tipo == 'M':
                if len(linea) != 4: raise ValueError("Merge requiere 4 valores.")
                entradas = [int(linea[2]), int(linea[3])]
                network.agregar_merge(id_nodo, entradas)
            else:
                print(f"Tipo de nodo desconocido: {tipo}. Ignorando.")

        # Lectura y Resolución de Consultas 
        print("\nConsultas (salida, índice):")
        resultados = []
        for i in range(q):
            try:
                linea = input(f"Consulta {i+1} (salida, k): ").split()
                if len(linea) != 2: raise ValueError("Consulta requiere 2 valores.")
                    
                id_salida_final = int(linea[0]) 
                k = int(linea[1]) 
                
                origen_global_pos = network.calcular_origen_global(id_salida_final, k)
                
                if origen_global_pos is None or origen_global_pos > network.m_global:
                    valor = "none"
                else:
                    valor = origen_global_pos 

                resultados.append(f"({id_salida_final}, {k}) -> {valor}")
                
            except Exception as e:

                resultados.append(f"Consulta {i+1} falló: Error de formato o nodo inválido. ({e})")

        # Mostrar Resultados 
        print("\n--- RESULTADOS ---")
        for res in resultados:
            print(res)

    except Exception as e:
        print(f"\nOcurrió un error general de entrada: {e}")

if __name__ == "__main__":
    resolver_splitstream()