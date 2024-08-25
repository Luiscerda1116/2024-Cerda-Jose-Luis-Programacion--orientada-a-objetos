import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}
        self.archivo = "inventario.txt"
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[int(id)] = Producto(int(id), nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(f"{producto}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
        self.guardar_inventario()

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()
            return True
        return False

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            return True
        return False

    def obtener_producto(self, id):
        return self.productos.get(id)

    def listar_productos(self):
        return list(self.productos.values())

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Ver producto")
    print("5. Listar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado exitosamente.")

        elif opcion == "2":
            id = int(input("ID del producto a actualizar: "))
            cantidad = int(input("Nueva cantidad (presione Enter para no cambiar): ") or None)
            precio = float(input("Nuevo precio (presione Enter para no cambiar): ") or None)
            if inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id = int(input("ID del producto a eliminar: "))
            if inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            id = int(input("ID del producto a ver: "))
            producto = inventario.obtener_producto(id)
            if producto:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            productos = inventario.listar_productos()
            if productos:
                for producto in productos:
                    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                print("No hay productos en el inventario.")

        elif opcion == "6":
            print("Gracias por usar el sistema de gestión de inventarios. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()