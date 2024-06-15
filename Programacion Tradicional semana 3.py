# Función para ingresar datos diarios de precipitaciones
def ingresar_precipitaciones_diarias():
    precipitaciones = []
    for i in range(7):
        precipitacion = float(input(f"Ingrese la precipitación del día {i+1} en mm: "))
        precipitaciones.append(precipitacion)
    return precipitaciones

# Función para calcular el promedio semanal de precipitaciones
def calcular_promedio_semanal(precipitaciones):
    if len(precipitaciones) == 0:
        return 0.0
    promedio = sum(precipitaciones) / len(precipitaciones)
    return promedio

# Función principal para ejecutar el programa
def main():
    print("Ingrese las precipitaciones diarias de la semana en milímetros:")
    precipitaciones = ingresar_precipitaciones_diarias()
    promedio = calcular_promedio_semanal(precipitaciones)
    print(f"El promedio semanal de precipitaciones es: {promedio:.2f} mm")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
