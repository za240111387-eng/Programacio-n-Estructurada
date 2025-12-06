def resolver_acertijo_esfinge():
    # El programa solicita las preguntas y resuelve el acertijo
    print("--- SOLUCIONADOR DEL ACERTIJO DE LA ESFINGE ---")
    print("El programa te dirá qué preguntar. Introduce la respuesta que te dé la Esfinge.\n")

    # Definición del sistema de preguntas (Axexes, Basiliscos, Centauros)
    preguntas = [
        (1, 0, 0),  # Pregunta 1: Patas de 1 Axex
        (0, 1, 0),  # Pregunta 2: Patas de 1 Basil
        (0, 0, 1),  # Pregunta 3: Patas de 1 Cent
        (1, 1, 1),  # Pregunta 4: Suma (1 de cada uno)
        (1, 2, 3)   # Pregunta 5: Suma ponderada
    ]

    respuestas = []

    # 1. Interacción: Recolección de datos
    for i, (a, b, c) in enumerate(preguntas, 1):
        print(f"PREGUNTA {i}: ¿Cuántas patas tienen {a} axexes, {b} basiliscos y {c} centauros?")
        while True:
            try:
                # Entrada de la respuesta de la Esfinge
                val = int(input(f"    >> Respuesta de la Esfinge {i}: "))
                if val < 0:
                    print("    Valor no negativo requerido.")
                    continue
                respuestas.append(val)
                break
            except ValueError:
                print("    Ingresa un número entero válido.")

    print("\nEvaluando la consistencia de las respuestas...\n")

    # 2. Solución: Búsqueda exhaustiva con redundancia
    # Premisa: solo una mentira (o ninguna).
    # Rango de 0 a 100 patas es suficiente para un problema de criaturas.
    rango_busqueda = range(101) 

    solucion_encontrada = None
    mentira_detectada = -1
    
    found = False
    for x in rango_busqueda:    # Patas Axexes
        if found: break
        for y in rango_busqueda:    # Patas Basiliscos
            if found: break
            for z in rango_busqueda: # Patas Centauros
                
                coincidencias = 0
                indice_fallo = -1
                
                # Verificación de la combinación (x, y, z) contra las 5 respuestas
                for i, (a, b, c) in enumerate(preguntas):
                    teorico = (a * x) + (b * y) + (c * z)
                    if teorico == respuestas[i]:
                        coincidencias += 1
                    else:
                        indice_fallo = i + 1 # Guarda el índice de la no-coincidencia
                
                # Si 4 o 5 respuestas coinciden, la solución es válida
                if coincidencias >= 4:
                    solucion_encontrada = (x, y, z)
                    mentira_detectada = indice_fallo if coincidencias == 4 else 0
                    found = True
                    break

    # 3. Presentación de resultados
    if solucion_encontrada:
        ax, ba, ce = solucion_encontrada
        print("-" * 30)
        print("¡SOLUCIÓN DESCIFRADA!")
        print("-" * 30)
        print(f"Axexes     : {ax} patas")
        print(f"Basiliscos : {ba} patas")
        print(f"Centauros  : {ce} patas")
        print("-" * 30)
        
        if mentira_detectada > 0:
            print(f"Falla detectada: Pregunta #{mentira_detectada}.")
            val_real = respuestas[mentira_detectada-1]
            # Recalcular el valor correcto
            a,b,c = preguntas[mentira_detectada-1]
            val_calc = (a*ax) + (b*ba) + (c*ce)
            print(f"Esfinge dijo: '{val_real}'. Valor real: '{val_calc}'.")
        else:
            print("Todas las respuestas fueron consistentes.")
            
    else:
        print("No se encontró una combinación lógica en el rango de búsqueda.")

if __name__ == "__main__":
    resolver_acertijo_esfinge()