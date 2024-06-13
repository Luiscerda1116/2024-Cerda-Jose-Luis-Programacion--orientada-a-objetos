# Función para ingresar los datos de los libros
def ingresar_libros():
    libros = []
    num_libros = int(input("Ingrese el número de libros: "))
    for _ in range(num_libros):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio = int(input("Ingrese el año de publicación: "))
        libro = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio
        }
        libros.append(libro)
    return libros

# Función para buscar libros por autor
def buscar_libros_por_autor(libros, autor):
    return [libro for libro in libros if libro["autor"].lower() == autor.lower()]

# Función principal
def main():
    libros = ingresar_libros()
    autor = input("Ingrese el autor a buscar: ")
    libros_encontrados = buscar_libros_por_autor(libros, autor)
    if libros_encontrados:
        print(f"Libros encontrados de {autor}:")
        for libro in libros_encontrados:
            print(f"Título: {libro['titulo']}, Año: {libro['anio']}")
    else:
        print(f"No se encontraron libros de {autor}.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
