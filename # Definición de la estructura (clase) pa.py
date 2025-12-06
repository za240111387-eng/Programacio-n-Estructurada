# Definición de la estructura (clase) para un estudiante
class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones
        self.promedio = sum(calificaciones) / len(calificaciones)
        self.estado = self._determinar_estado()

    def _determinar_estado(self):
        if self.promedio > 7.0:
            return "Pasa de grado"
        elif self.promedio > 6.0 and self.promedio <= 7.0:
            return "Recuperacion"
        else:
            return "Repite curso"

def main():
    num_estudiantes = int(input("¿Cuántos estudiantes desea evaluar? "))

    estudiantes = []
    
    promedio_mas_alto = -1.0
    mejor_estudiante = None # Para el promedio más alto
    
    print("\n--- Sistema de Evaluacion Escolar ---")
    
    for i in range(num_estudiantes):
        print(f"\nDatos del Estudiante {i + 1}:")
        nombre = input("Nombre: ")
        
        calificaciones = []
        print("Ingrese las 5 calificaciones:")
        for j in range(5):
            while True: # Bucle para 
                 que se ingresen calificaciones válidas
                try:
                    calificacion = float(input(f"Materia {j + 1}: "))
                    if 0 <= calificacion <= 10: # O el rango de calificaciones que consideres
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("Por favor, ingrese una calificación entre 0 y 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        
        # Creamos un objeto Estudiante
        nuevo_estudiante = Estudiante(nombre, calificaciones)
        estudiantes.append(nuevo_estudiante)
        
        # Comparamos para encontrar al mejor estudiante
        if nuevo_estudiante.promedio > promedio_mas_alto:
            promedio_mas_alto = nuevo_estudiante.promedio
            mejor_estudiante = nuevo_estudiante # Guardamos el objeto completo
            
    print("\n--- Resumen de Resultados ---")
    print(f"{'Nombre':<20} {'Promedio':<10} {'Estado':<20}")
    print("-" * 50)
    
    for estudiante in estudiantes:
        print(f"{estudiante.nombre:<20} {estudiante.promedio:<10.2f} {estudiante.estado:<20}")
        
    print("\n--- Atencion Especial ---")
    requieren_atencion = False
    for estudiante in estudiantes:
        if estudiante.estado == "Recuperacion" or estudiante.estado == "Repite curso":
            print(f"- {estudiante.nombre}: necesita atencion academica especial.")
            requieren_atencion = True
    
    if not requieren_atencion:
        print("Ningún estudiante requiere atención académica especial en este momento.")

    if mejor_estudiante: # Verificamos si se encontró un mejor estudiante
        print(f"\n*** Mejor Estudiante: {mejor_estudiante.nombre} (Promedio: {mejor_estudiante.promedio:.2f}) ***")
    
if __name__ == "__main__":
    main()