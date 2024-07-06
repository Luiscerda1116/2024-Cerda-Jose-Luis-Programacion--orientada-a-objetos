# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0  # Atributo encapsulado

    def arrancar(self):
        print(f"{self.marca} {self.modelo} arrancando.")

    def detener(self):
        print(f"{self.marca} {self.modelo} detenido.")

    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, km):
        if km >= 0:
            self.__kilometraje = km
        else:
            print("El kilometraje no puede ser negativo.")

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Método sobrescrito (polimorfismo)
    def arrancar(self):
        print(f"Coche {self.marca} {self.modelo} arrancando. Tiene {self.puertas} puertas.")

    def abrir_maletero(self):
        print(f"Abriendo maletero del coche {self.marca} {self.modelo}.")

# Clase derivada con polimorfismo de argumentos múltiples
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo=""):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def wheelie(self, duracion=2):
        print(f"Haciendo un wheelie de {duracion} segundos con la moto {self.marca} {self.modelo}.")

# Programa principal
if __name__ == "__main__":
    # Creando instancias
    coche1 = Coche("Toyota", "Corolla", 4)
    moto1 = Motocicleta("Honda", "CBR600RR", "Deportiva")

    # Usando métodos de las clases
    coche1.arrancar()
    coche1.abrir_maletero()
    coche1.detener()

    moto1.arrancar()
    moto1.wheelie()
    moto1.wheelie(5)

    # Demostrando encapsulación
    print(f"Kilometraje del coche: {coche1.get_kilometraje()} km")
    coche1.set_kilometraje(100)
    print(f"Nuevo kilometraje del coche: {coche1.get_kilometraje()} km")
    coche1.set_kilometraje(-50)  # Esto mostrará un mensaje de error