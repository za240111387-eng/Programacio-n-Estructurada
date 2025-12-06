from itertools import product
from typing import List, Tuple


def validar_y_parsear_dados(mensaje: str) -> List[int]:
   
    while True:
        try:
            linea = input(mensaje).strip()
            partes = list(map(int, linea.split()))
            
            if not partes:
                raise ValueError("La entrada está vacía.")
            
            num_caras = partes[0]
            caras = partes[1:]
            
            if len(caras) != num_caras:
                raise ValueError(f"El número de caras declarado ({num_caras}) no coincide con los valores dados ({len(caras)}).")
            
            if not all(c >= 1 for c in caras):
                 raise ValueError("Todos los valores de las caras deben ser mayores o iguales a 1, según el enunciado.")
            
            return caras
            
        except ValueError as e:
            print(f"❌ Error en la entrada: {e}. Inténtalo de nuevo.")

def calcular_puntuacion(dado_a: List[int], dado_b: List[int]) -> float:
 
    victorias_a = 0
    empates = 0
    
    for cara_a in dado_a:
        for cara_b in dado_b:
            if cara_a > cara_b:
                victorias_a += 1
            elif cara_a == cara_b:
                empates += 1
                
    total_tiradas = len(dado_a) * len(dado_b)
    if total_tiradas == 0:
        return 0.0
        
    score = (victorias_a + 0.5 * empates) / total_tiradas
    return score



def buscar_puntuaciones_extremas(d1: List[int], d2: List[int], num_caras_d3: int, max_valor_cara: int) -> Tuple[float, float]:
  
    
    posibles_caras = range(1, max_valor_cara + 1)
    espacio_tamano = len(posibles_caras) ** num_caras_d3
    
    print(f"\nIniciando búsqueda exhaustiva de D3:")
    print(f"  - Caras de D3 (N): {num_caras_d3}")
    print(f"  - Valor Máximo (M): {max_valor_cara}")
    print(f"  - Espacio total: {espacio_tamano:,} combinaciones.")
    
  
    min_score_d3_vs_d2 = 1.0  
    max_score_d3_vs_d1 = 0.0  
    
   
    for d3 in product(posibles_caras, repeat=num_caras_d3):
        d3_list = list(d3)
        
        
        score_d3_vs_d2 = calcular_puntuacion(d3_list, d2)
        if score_d3_vs_d2 < min_score_d3_vs_d2:
            min_score_d3_vs_d2 = score_d3_vs_d2
            
       
        score_d3_vs_d1 = calcular_puntuacion(d3_list, d1)
        if score_d3_vs_d1 > max_score_d3_vs_d1:
            max_score_d3_vs_d1 = score_d3_vs_d1
            
    return min_score_d3_vs_d2, max_score_d3_vs_d1



def ejecutar_solucion_dados():
    
    print(" Problema 2: Dados Intransitivos ")
    
    
    print("\n Configuración de la Búsqueda de D3 ")
    while True:
        try:
            n_caras = int(input("Ingrese el número de caras (N) de D3 a buscar (Ej: 6): "))
            m_valor = int(input("Ingrese el valor MÁXIMO (M) de las caras de D3 (Ej: 9): "))
            
            if n_caras < 1 or m_valor < 1:
                raise ValueError("N y M deben ser mayores o iguales a 1.")
            
            if (m_valor ** n_caras) > 1000000 and (n_caras * m_valor > 60):
                print(" Advertencia: El espacio de búsqueda es muy grande (> 1 millón). Esto puede tardar mucho.")
            
            break
        except ValueError as e:
            print(f"ntrada inválida: {e}. Inténtelo de nuevo.")

    
    print("\n¿Deseas usar el ejemplo provisto o ingresar tus datos?")
    opcion = input("Escribe 'ejemplo': ").strip().lower()

    if opcion == 'ejemplo':
        
        d1_caras = [1, 1, 6, 6, 8, 8]
        d2_caras = [2, 4, 9]
        print("\nCargando datos del ejemplo:")
        print(f"D1: {len(d1_caras)} {d1_caras}")
        print(f"D2: {len(d2_caras)} {d2_caras}")
    else:
       
        d1_caras = validar_y_parsear_dados("\nEntrada D1 (N c1 c2 ...): ")
        d2_caras = validar_y_parsear_dados("Entrada D2 (N c1 c2 ...): ")
    
  
    p_d1_vs_d2 = calcular_puntuacion(d1_caras, d2_caras)
    
    print(f"\nVerificación inicial: P(D1 gana o empata D2) = {p_d1_vs_d2:.9f}")
    
    if p_d1_vs_d2 <= 0.5:
        print("Advertencia: D1 NO tiene ventaja sobre D2. Esto contradice la premisa inicial.")

    
    try:
        min_d3_vs_d2, max_d3_vs_d1 = buscar_puntuaciones_extremas(d1_caras, d2_caras, n_caras, m_valor)

    
        print("\n" + "=" * 50)
        print("RESULTADOS FINALES (Puntuaciones Extremas)")
        print("=" * 50)
        
        
        print(f"Puntuación MÍNIMA de D3 vs D2: {min_d3_vs_d2:.9f}")
        
        
        print(f"Puntuación MÁXIMA de D3 vs D1: {max_d3_vs_d1:.9f}")
        
        
        if opcion == 'ejemplo' and n_caras == 6 and m_valor == 9:
            print("\nResultado esperado para este ejemplo y configuración: 0.291666667 0.750000000")

    except Exception as e:
        print(f"\nOcurrió un error grave durante el cálculo: {e}")

if __name__ == "__main__":
    ejecutar_solucion_dados()