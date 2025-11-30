def solve_lights(num_lights, num_buttons, colors, btn_controls):
    # Mapeo de colores a valores: R=0, G=1, B=2
    val_map = {'R': 0, 'G': 1, 'B': 2}
    
    # Determinamos qué botones controlan cada luz (Inversión de la entrada)
    light_to_btns = [[] for _ in range(num_lights)]
    for b_idx, lights in enumerate(btn_controls):
        for l_idx in lights:
            light_to_btns[l_idx].append(b_idx)

    # Construcción del grafo de restricciones entre botones
    adj = [[] for _ in range(num_buttons)]
    # Restricciones para botones individuales (cuando una luz solo tiene 1 botón)
    self_constraints = {} 

    for l_idx, btns in enumerate(light_to_btns):
        current_color = val_map[colors[l_idx]]
        # Cuánto falta para llegar a 0 (Rojo)
        needed = (3 - current_color) % 3

        if len(btns) == 0:
            if needed != 0: return "Impossible"
        elif len(btns) == 1:
            u = btns[0]
            if u in self_constraints and self_constraints[u] != needed:
                return "Impossible"
            self_constraints[u] = needed
        elif len(btns) == 2:
            u, v = btns
            # La arista guarda el vecino y la suma necesaria entre ambos
            adj[u].append((v, needed))
            adj[v].append((u, needed))

    # Resolver componentes conexos
    visited = [False] * num_buttons
    total_presses = 0

    for i in range(num_buttons):
        if not visited[i]:
            component_nodes = []
            q_comp = [i]
            visited[i] = True
            
            # BFS simple para identificar todos los nodos del componente actual
            idx = 0
            while idx < len(q_comp):
                u = q_comp[idx]
                idx += 1
                component_nodes.append(u)
                for v, _ in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q_comp.append(v)

            # Probar las 3 posibilidades (0, 1, 2) para el primer nodo del componente
            best_local_sum = float('inf')
            possible = False

            for start_val in range(3):
                # Diccionario para guardar el estado actual de esta prueba
                states = {component_nodes[0]: start_val}
                valid = True
                stack = [component_nodes[0]]
                
                # Propagación de valores (DFS iterativo)
                while stack:
                    u = stack.pop()
                    val_u = states[u]

                    # Verificar restricción propia si existe
                    if u in self_constraints:
                        if val_u != self_constraints[u]:
                            valid = False
                            break
                    
                    # Verificar vecinos
                    for v, req in adj[u]:
                        target_v = (req - val_u) % 3
                        if v in states:
                            if states[v] != target_v:
                                valid = False
                                break
                        else:
                            states[v] = target_v
                            stack.append(v)
                    
                    if not valid: break
                
                # Verificar que todos los nodos del componente tengan valor asignado
                if valid and len(states) == len(component_nodes):
                    current_sum = sum(states.values())
                    if current_sum < best_local_sum:
                        best_local_sum = current_sum
                        possible = True

            if not possible:
                return "Impossible"
            total_presses += best_local_sum

    return total_presses

# --- Bloque de Prueba ---

if __name__ == "__main__":
    # Ejemplo del problema
    # 3 luces, 3 botones. Estado inicial RGB.
    # Botón 0 controla luces [0, 1]
    # Botón 1 controla luces [1, 2]
    # Botón 2 controla luces [2, 0]
    
    L = 3
    B = 3
    S = "RGB"
    # Lista de listas: indice i contiene las luces del botón i
    conns = [[0, 1], [1, 2], [2, 0]]

    res = solve_lights(L, B, S, conns)
    print(f"Pulsaciones mínimas: {res}")