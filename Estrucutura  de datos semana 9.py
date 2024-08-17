class Articulo:
    def __init__(self, codigo, descripcion, stock, valor):
        self.codigo = codigo
        self.descripcion = descripcion
        self.stock = stock
        self.valor = valor

    def __repr__(self):
        return f"Artículo: {self.descripcion} (Código: {self.codigo}) - Stock: {self.stock}, Valor: ${self.valor:.2f}"


class GestorAlmacen:
    def __init__(self):
        self.catalogo = {}

    def incorporar_articulo(self, articulo):
        if articulo.codigo not in self.catalogo:
            self.catalogo[articulo.codigo] = articulo
            print("Artículo incorporado exitosamente.")
        else:
            print("Error: Ya existe un artículo con ese código.")

    def retirar_articulo(self, codigo):
        if codigo in self.catalogo:
            del self.catalogo[codigo]
            print("Artículo retirado del catálogo.")
        else:
            print("Error: No se encontró el artículo con ese código.")

    def modificar_articulo(self, codigo, nuevo_stock=None, nuevo_valor=None):
        if codigo in self.catalogo:
            if nuevo_stock is not None:
                self.catalogo[codigo].stock = nuevo_stock
            if nuevo_valor is not None:
                self.catalogo[codigo].valor = nuevo_valor
            print("Artículo actualizado correctamente.")
        else:
            print("Error: No se encontró el artículo con ese código.")

    def localizar_articulo(self, descripcion):
        encontrados = [art for art in self.catalogo.values() if descripcion.lower() in art.descripcion.lower()]
        if encontrados:
            for art in encontrados:
                print(art)
        else:
            print("No se encontraron artículos que coincidan con la descripción.")

    def listar_catalogo(self):
        if self.catalogo:
            for articulo in self.catalogo.values():
                print(articulo)
        else:
            print("El catálogo está vacío.")


def interfaz_usuario():
    gestor = GestorAlmacen()
    while True:
        print("\n--- Gestor de Almacén ---")
        print("1. Incorporar artículo")
        print("2. Retirar artículo")
        print("3. Modificar artículo")
        print("4. Localizar artículo")
        print("5. Listar catálogo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del artículo: ")
            descripcion = input("Descripción: ")
            stock = int(input("Stock inicial: "))
            valor = float(input("Valor: "))
            articulo = Articulo(codigo, descripcion, stock, valor)
            gestor.incorporar_articulo(articulo)

        elif opcion == "2":
            codigo = input("Código del artículo a retirar: ")
            gestor.retirar_articulo(codigo)

        elif opcion == "3":
            codigo = input("Código del artículo a modificar: ")
            nuevo_stock = input("Nuevo stock (presione Enter para no cambiar): ")
            nuevo_valor = input("Nuevo valor (presione Enter para no cambiar): ")
            gestor.modificar_articulo(codigo,
                                      int(nuevo_stock) if nuevo_stock else None,
                                      float(nuevo_valor) if nuevo_valor else None)

        elif opcion == "4":
            descripcion = input("Descripción del artículo a buscar: ")
            gestor.localizar_articulo(descripcion)

        elif opcion == "5":
            gestor.listar_catalogo()

        elif opcion == "6":
            print("Gracias por usar el Gestor de Almacén. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    interfaz_usuario()