class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.info[0]

    @property
    def autor(self):
        return self.info[1]

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros con ISBN como clave
        self.usuarios = set()  # Conjunto de IDs de usuario
        self.usuarios_obj = {}  # Diccionario de objetos Usuario con ID como clave

    def anadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            return True
        return False

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_obj[usuario.id_usuario] = usuario
            return True
        return False

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_obj[id_usuario]
            return True
        return False

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            usuario = self.usuarios_obj[id_usuario]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios_obj[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    return True
        return False

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == 'titulo' and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios_obj[id_usuario].libros_prestados
        return []

# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "9780307474728")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "9780156012195")
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María López", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("9780307474728", "U001")
biblioteca.prestar_libro("9780156012195", "U002")

# Buscar libros
print("Búsqueda por título 'principito':")
for libro in biblioteca.buscar_libros('titulo', 'principito'):
    print(f"{libro.titulo} por {libro.autor}")

# Listar libros prestados
print("\nLibros prestados a Juan Pérez:")
for libro in biblioteca.listar_libros_prestados("U001"):
    print(f"{libro.titulo} por {libro.autor}")

# Devolver un libro
biblioteca.devolver_libro("9780307474728", "U001")

print("\nLibros prestados a Juan Pérez después de la devolución:")
for libro in biblioteca.listar_libros_prestados("U001"):
    print(f"{libro.titulo} por {libro.autor}")