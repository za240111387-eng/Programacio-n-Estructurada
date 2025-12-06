from itertools import product
from typing import List, Tuple, Optional



def resolver_sistema_luces():
   
    print(" Sistema de Luces Inteligente (GF(2))")

    
    try:
        n, m = map(int, input("Ingrese n (luces) y m (interruptores): ").split())
        
        # Validación de longitud básica para estados
        estado_inicial_str = input(f"Estado inicial de {n} luces (ej: 0 1 0): ").split()
        if len(estado_inicial_str) != n: raise ValueError("Número incorrecto de estados iniciales.")
        estado_inicial = list(map(int, estado_inicial_str))
        
        estado_deseado_str = input(f"Estado deseado de {n} luces (ej: 1 0 1): ").split()
        if len(estado_deseado_str) != n: raise ValueError("Número incorrecto de estados deseados.")
        estado_deseado = list(map(int, estado_deseado_str))
        
        print(f"Ingrese las conexiones (líneas m, formato: [luz1] [luz2]...) usando índices de luz 1-based.")
        conexiones: List[List[int]] = []
        for j in range(m):
            conexiones.append(list(map(int, input(f"Interruptor {j+1}: ").split())))

    except ValueError as e:
        print(f"error en el formato de entrada: {e}. Asegúrese de usar números enteros y el formato correcto.")
        return

   
    target = [estado_deseado[k] ^ estado_inicial[k] for k in range(n)]

   
    A_aumentada: List[List[int]] = []
    for k in range(n):
        fila_A = [0] * m
        for j in range(m):
           
            if k + 1 in conexiones[j]:
                fila_A[j] = 1
        fila_A.append(target[k])
        A_aumentada.append(fila_A)

    
    
    n_filas = len(A_aumentada)
    n_cols = len(A_aumentada[0])
    m_variables = n_cols - 1
    
    col_pivote = []
    fila_actual = 0
    
   
    for col_j in range(m_variables):
        
        
        pivote_fila = fila_actual
        while pivote_fila < n_filas and A_aumentada[pivote_fila][col_j] == 0:
            pivote_fila += 1
            
        if pivote_fila < n_filas:
            
            A_aumentada[fila_actual], A_aumentada[pivote_fila] = A_aumentada[pivote_fila], A_aumentada[fila_actual]
            
            
            for fila_k in range(n_filas):
                if fila_k != fila_actual and A_aumentada[fila_k][col_j] == 1:
                    # Fila k = Fila k XOR Fila actual
                    for l in range(n_cols):
                        A_aumentada[fila_k][l] ^= A_aumentada[fila_actual][l]
            
            col_pivote.append(col_j)
            fila_actual += 1

    
    for i in range(fila_actual, n_filas):
        if A_aumentada[i][m_variables] == 1:
            print("\n--- RESULTADO FINAL ---")
            print("impossible")
            return

    
    
    
    col_libre = [j for j in range(m_variables) if j not in col_pivote]
    num_vars_libres = len(col_libre)
    
    
    
    xp = [0] * m_variables
    for i in range(len(col_pivote)):
        xp[col_pivote[i]] = A_aumentada[i][m_variables]
        
    null_basis = []
    for col_j in col_libre:
        xj = [0] * m_variables
        xj[col_j] = 1
        for i in range(len(col_pivote)):
            xj[col_pivote[i]] = A_aumentada[i][col_j]
        null_basis.append(xj)
        
    
    min_peso = m + 1
    
    if num_vars_libres > 20:
        print(f"\n Advertencia: {num_vars_libres} variables libres. La búsqueda (2^{num_vars_libres}) podría tardar mucho.")

    for combinacion in product([0, 1], repeat=num_vars_libres):
        x_candidato = list(xp)
        
        
        for idx_libre in range(num_vars_libres):
            c_j = combinacion[idx_libre]
            if c_j == 1:
                base = null_basis[idx_libre]
                for k in range(m_variables):
                    x_candidato[k] ^= base[k]
                    
        min_peso = min(min_peso, sum(x_candidato))

    
    print("\n--- RESULTADO FINAL ---")
    print(f"Número mínimo de activaciones: {min_peso}")

if __name__ == "__main__":
    resolver_sistema_luces()