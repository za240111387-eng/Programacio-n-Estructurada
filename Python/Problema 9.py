import sys

# ----DATOS--------------------------------------
input_texto = """
3 3
Leon
Tigre
Oso
Tigre
Oso
Leon
0 1
1 2
2 0
"""
# -------------------------------------------------

def main():

    input_data = input_texto.split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        # 1. Leer número de recintos (N) y túneles (M)
        n = int(next(iterator))
        m = int(next(iterator))
        
        # 2. Leer configuración INICIAL de animales
        A = [next(iterator) for _ in range(n)]
        
        # 3. Leer configuración DESEADA de animales
        B = [next(iterator) for _ in range(n)]
        
        # 4. Construir el grafo
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            # NOTA: Si en tu examen los nodos empiezan en 1, descomenta esto:
            # u -= 1
            # v -= 1
            adj[u].append(v)
            adj[v].append(u)
            
    except StopIteration:
        return

    vis = [False] * n
    
    # Función para explorar zonas conectadas
    def get_component(u, nodes):
        vis[u] = True
        nodes.append(u)
        for v in adj[u]:
            if not vis[v]:
                get_component(v, nodes)

    # Lógica principal
    for i in range(n):
        if not vis[i]:
            nodes = []
            get_component(i, nodes)
            
            # Conexiones 
            edges = 0
            for u in nodes:
                edges += len(adj[u])
            edges //= 2
            
            # REGLA 1: Si es un Árbol (pocas conexiones), es rígido.
            # Los animales no se pueden cruzar. Deben estar ya en su sitio.
            if edges < len(nodes):
                for u in nodes:
                    if A[u] != B[u]:
                        print("impossible")
                        return
            
            # REGLA 2: Si hay Ciclos (suficientes conexiones), es flexible.
            # Solo importa que el grupo de animales sea el mismo (aunque desordenado).
            else:
                list1 = [A[u] for u in nodes]
                list2 = [B[u] for u in nodes]
                list1.sort()
                list2.sort()
                
                if list1 != list2:
                    print("impossible")
                    return

    print("possible")