class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def ingresar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio = int(input("Ingrese el año de publicación: "))
        libro = Libro(titulo, autor, anio)
        self.libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor.lower() == autor.lower()]

    def mostrar_libros(self, libros):
        if libros:
            for libro in libros:
                print(libro)
        else:
            print("No se encontraron libros.")

# Función principal
def main():
    biblioteca = Biblioteca()
    num_libros = int(input("Ingrese el número de libros: "))
    for _ in range(num_libros):
        biblioteca.ingresar_libro()
    
    autor = input("Ingrese el autor a buscar: ")
    libros_encontrados = biblioteca.buscar_libros_por_autor(autor)
    biblioteca.mostrar_libros(libros_encontrados)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
