# Este programa convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
# Utiliza funciones para cada tipo de conversión y maneja diferentes tipos de datos.

def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def celsius_a_kelvin(celsius):
    """
    Convierte temperatura de Celsius a Kelvin.
    """
    return celsius + 273.15


def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte temperatura de Fahrenheit a Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_a_kelvin(fahrenheit):
    """
    Convierte temperatura de Fahrenheit a Kelvin.
    """
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_a_celsius(kelvin):
    """
    Convierte temperatura de Kelvin a Celsius.
    """
    return kelvin - 273.15


def kelvin_a_fahrenheit(kelvin):
    """
    Convierte temperatura de Kelvin a Fahrenheit.
    """
    return (kelvin - 273.15) * 9 / 5 + 32


def main():
    continuar = True

    while continuar:
        print("\nConversor de Temperatura")
        print("1. Celsius a Fahrenheit")
        print("2. Celsius a Kelvin")
        print("3. Fahrenheit a Celsius")
        print("4. Fahrenheit a Kelvin")
        print("5. Kelvin a Celsius")
        print("6. Kelvin a Fahrenheit")
        print("7. Salir")

        # Solicitamos la opción al usuario
        opcion = input("Seleccione una opción (1-7): ")

        if opcion in ['1', '2', '3', '4', '5', '6']:
            temperatura = float(input("Ingrese la temperatura: "))

            if opcion == '1':
                resultado = celsius_a_fahrenheit(temperatura)
                print(f"{temperatura}°C es igual a {resultado:.2f}°F")
            elif opcion == '2':
                resultado = celsius_a_kelvin(temperatura)
                print(f"{temperatura}°C es igual a {resultado:.2f}K")
            elif opcion == '3':
                resultado = fahrenheit_a_celsius(temperatura)
                print(f"{temperatura}°F es igual a {resultado:.2f}°C")
            elif opcion == '4':
                resultado = fahrenheit_a_kelvin(temperatura)
                print(f"{temperatura}°F es igual a {resultado:.2f}K")
            elif opcion == '5':
                resultado = kelvin_a_celsius(temperatura)
                print(f"{temperatura}K es igual a {resultado:.2f}°C")
            elif opcion == '6':
                resultado = kelvin_a_fahrenheit(temperatura)
                print(f"{temperatura}K es igual a {resultado:.2f}°F")
        elif opcion == '7':
            print("Gracias por usar el conversor de temperatura.")
            continuar = False
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()