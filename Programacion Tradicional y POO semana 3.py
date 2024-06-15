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

Programación Orienda a objetos
class RegistroPrecipitaciones:
    def __init__(self):
        self.precipitaciones = []

    def ingresar_precipitacion_diaria(self, precipitacion):
        self.precipitaciones.append(precipitacion)

    def ingresar_precipitaciones_semana(self):
        for i in range(7):
            precipitacion = float(input(f"Ingrese la precipitación del día {i+1} en mm: "))
            self.ingresar_precipitacion_diaria(precipitacion)

    def calcular_promedio_semanal(self):
        if len(self.precipitaciones) == 0:
            return 0.0
        promedio = sum(self.precipitaciones) / len(self.precipitaciones)
        return promedio

# Ejemplo de uso
def main():
    registro = RegistroPrecipitaciones()
    print("Ingrese las precipitaciones diarias de la semana en milímetros:")
    registro.ingresar_precipitaciones_semana()
    promedio = registro.calcular_promedio_semanal()
    print(f"El promedio semanal de precipitaciones es: {promedio:.2f} mm")

if __name__ == "__main__":
    main()
