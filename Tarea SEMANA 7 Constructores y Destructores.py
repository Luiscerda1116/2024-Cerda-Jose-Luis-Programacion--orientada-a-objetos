import time

class Archivo:
    def __init__(self, nombre, modo='r'):
        """
        Constructor de la clase Archivo.
        Inicializa un objeto Archivo y abre el archivo especificado.

        :param nombre: Nombre del archivo a abrir
        :param modo: Modo de apertura del archivo (por defecto, lectura)
        """
        self.nombre = nombre
        self.modo = modo
        self.archivo = None
        try:
            self.archivo = open(self.nombre, self.modo)
            print(f"Archivo '{self.nombre}' abierto en modo '{self.modo}'")
        except IOError:
            print(f"Error al abrir el archivo '{self.nombre}'")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se encarga de cerrar el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado")

class Temporizador:
    def __init__(self):
        """
        Constructor de la clase Temporizador.
        Inicializa el tiempo de inicio del temporizador.
        """
        self.tiempo_inicio = time.time()
        print("Temporizador iniciado")

    def __del__(self):
        """
        Destructor de la clase Temporizador.
        Calcula y muestra el tiempo transcurrido desde la creación del objeto.
        """
        tiempo_transcurrido = time.time() - self.tiempo_inicio
        print(f"Temporizador finalizado. Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")

# Demostración de uso
def main():
    # Uso de la clase Archivo
    archivo = Archivo("ejemplo.txt", "w")
    if archivo.archivo:
        archivo.archivo.write("Hola, mundo!")
    # El destructor se llamará automáticamente al salir del scope

    # Uso de la clase Temporizador
    temporizador = Temporizador()
    time.sleep(2)  # Simulamos alguna operación que lleva tiempo
    # El destructor se llamará automáticamente al salir del scope

if __name__ == "__main__":
    main()