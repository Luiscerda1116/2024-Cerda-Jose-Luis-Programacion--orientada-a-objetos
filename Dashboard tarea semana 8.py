import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo de código especificado por la ruta.

    :param ruta_script: Ruta relativa o absoluta del archivo de código.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def ejecutar_script(ruta_script):
    """
    Ejecuta el script especificado por la ruta.

    :param ruta_script: Ruta relativa o absoluta del archivo de script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            script = archivo.read()
            exec(script)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")


def mostrar_menu():
    """
    Muestra el menú principal y permite al usuario seleccionar una opción para ver o ejecutar scripts.
    """
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {os.path.basename(opciones[key])}")
        print("E - Ejecutar un script")
        print("0 - Salir")

        eleccion = input("Elige una opción para ver su código, 'E' para ejecutar un script o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        elif eleccion.lower() == 'e':
            ruta_script = input("Introduce la ruta del script a ejecutar: ")
            ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
