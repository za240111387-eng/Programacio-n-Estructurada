from typing import List, Tuple, Dict, Set

# Constantes del juego
NUM_JUGADORES = 4      
NUM_CONJUNTOS = 8      
NUM_CARTAS_INDICES = 4 


EJEMPLO_ACCIONES_TRAMPA = [
    # 1. Petición válida inicial (asumimos 0 tiene una carta del set 5)
    "ask 0 1 5 0",
    # 2. 1 niega tenerla (1 ya no es dueño posible de 5, 0)
    "deny 0 1 5 0", 
    # 3. 0 pide otra carta a 2
    "ask 0 2 5 1",
    # 4. 2 se la da a 0 (0 ahora tiene con certeza 5, 1)
    "give 0 2 5 1", 
    # 5. TRAMPA: 3 pide carta del set 6, pero es imposible que 3 tenga alguna carta del set 6.
    "ask 3 0 6 3", # <--- TRAMPA AQUÍ (Regla 1)
    # 6. Cuarteto
    "quartet 0 5"
]


def detectar_trampa_simple():
    """
    Simula el juego de Cuartetos con opción de cargar peticiones predefinidas.
    """
    

    duenos_posibles: Dict[Tuple[int, int], Set[int]] = { 
        (s, c): {0, 1, 2, 3} 
        for s in range(NUM_CONJUNTOS) 
        for c in range(NUM_CARTAS_INDICES) 
    }

    retirado: List[bool] = [False] * NUM_CONJUNTOS
    accion_num = 0

    def verificar_contradiccion() -> bool:
        """Verifica si alguna carta no tiene dueño posible."""
        for _, posibles in duenos_posibles.items():
            if len(posibles) == 0:
                return True
        return False
    
   
    print("--- 🕵️‍♀️ DETECCIÓN DE TRAMPA EN CUARTETOS (Simple) 🕵️‍♀️ ---")
    print("Jugadores: 0-3 | Sets: 0-7 | Cartas (Índice): 0-3")
    
    opcion = input("\n¿Deseas 'ingresar' acciones o 'cargar' el ejemplo de trampa? ").strip().lower()

    if opcion == 'cargar':
        acciones_a_procesar = EJEMPLO_ACCIONES_TRAMPA
        print("\nCargando acciones predefinidas...")
    else:
        print("\nModo de ingreso interactivo. Escribe 'FIN' para terminar el análisis.")
        acciones_a_procesar = []
        
        # Bucle para ingreso interactivo
        while True:
            linea = input(f"Acción {len(acciones_a_procesar) + 1}: ").strip().upper()
            if linea == 'FIN':
                break
            if linea:
                acciones_a_procesar.append(linea)


    
    
    for linea in acciones_a_procesar:
        accion_num += 1
        
        try:
            partes = linea.lower().split()
            if not partes: continue 
            
            tipo = partes[0]
            
          
            if tipo == "ask" or tipo == "give" or tipo == "deny":
                if len(partes) != 5: raise ValueError("Formato de 5 elementos incorrecto.")
                A, B, s, c = map(int, partes[1:])
                if not (0 <= A < NUM_JUGADORES and 0 <= B < NUM_JUGADORES and 0 <= s < NUM_CONJUNTOS and 0 <= c < NUM_CARTAS_INDICES):
                    raise ValueError("Índices fuera de rango.")
                ac = (tipo, A, B, s, c)
                
            elif tipo == "quartet":
                if len(partes) != 3: raise ValueError("Formato de 3 elementos incorrecto.")
                A, s = map(int, partes[1:])
                if not (0 <= A < NUM_JUGADORES and 0 <= s < NUM_CONJUNTOS):
                    raise ValueError("Índices fuera de rango.")
                ac = (tipo, A, s)
                
            else:
                raise ValueError(f"Tipo de acción '{tipo}' no reconocido.")

        except ValueError as e:
            print(f"Error de formato en Acción {accion_num}: {e}. Skipping.")
            continue
        
        print(f"-> Procesando Acción {accion_num}: {' '.join(partes)}")


        
        
        if tipo == "ask":
            A, B, s, c = ac[1:]
            
            
            alguna_posible = any(A in duenos_posibles[(s, carta_idx)] for carta_idx in range(NUM_CARTAS_INDICES))

            if not alguna_posible:
                print(f"rampa (Regla 1: Petición Ilegal) detectada.")
                return f"no {accion_num}"
        
        
        elif tipo == "give":
            A, B, s, c = ac[1:]

            if B not in duenos_posibles[(s, c)]:
                print(f"rampa (Lógica: Entrega Imposible) detectada.")
                return f"no {accion_num}"

          
            duenos_posibles[(s, c)] = {A}

        
        elif tipo == "deny":
            A, B, s, c = ac[1:]

            if B in duenos_posibles[(s, c)]:
                duenos_posibles[(s, c)].remove(B)

            
            if verificar_contradiccion():
                 print(f"❌ Trampa (Regla 2: Mentira/Negación Imposible) detectada.")
                 return f"no {accion_num}"

        
        elif tipo == "quartet":
            A, s = ac[1:]
            
            if retirado[s]:
                 print(f"Trampa (Lógica: Cuarteto Duplicado) detectada.")
                 return f"no {accion_num}"
                 
            for c in range(NUM_CARTAS_INDICES):
                carta = (s, c)
                
                if A not in duenos_posibles[carta]:
                    print(f"❌ Trampa (Lógica: Cuarteto Incompleto) detectada.")
                    return f"no {accion_num}"
                
                
                duenos_posibles[carta] = {A} 
                
            retirado[s] = True

    
        if verificar_contradiccion():
             print(f"Trampa (Contradicción Lógica Global) detectada.")
             return f"no {accion_num}"

    
    return "yes"


if __name__ == "__main__":
    resultado = detectar_trampa_simple()
    print("\n--- RESULTADO FINAL DEL ANÁLISIS ---")
    print(resultado)