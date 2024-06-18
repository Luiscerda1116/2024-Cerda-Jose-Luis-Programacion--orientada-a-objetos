# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo  # Código del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.stock = stock  # Cantidad en stock

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}) - Precio: ${self.precio} - Stock: {self.stock}"

# Clase que representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Email del cliente

    def __str__(self):
        return f"Cliente: {self.nombre} - Email: {self.email}"

# Clase que representa un pedido en la tienda
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente  # Objeto de la clase Cliente
        self.productos = []  # Lista de productos en el pedido
        self.total = 0  # Total del pedido

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
            producto.stock -= cantidad
            self.total += producto.precio * cantidad
        else:
            print(f"Error: No hay suficiente stock de {producto.nombre}.")

    def __str__(self):
        detalles_productos = "\n".join([f"{prod.nombre} x{cant}" for prod, cant in self.productos])
        return f"Pedido de {self.cliente.nombre}\nProductos:\n{detalles_productos}\nTotal: ${self.total}"

# Clase que representa la tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tienda
        self.productos = []  # Lista de productos disponibles en la tienda

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto)

    def crear_pedido(self, cliente):
        return Pedido(cliente)

# Creación de la tienda y productos
mi_tienda = Tienda("Tienda Online")

mi_tienda.agregar_producto(Producto(1, "Laptop", 1000, 10))
mi_tienda.agregar_producto(Producto(2, "Mouse", 50, 50))
mi_tienda.agregar_producto(Producto(3, "Teclado", 80, 30))

# Listar productos disponibles
mi_tienda.listar_productos()

# Creación de un cliente y pedido
cliente = Cliente("Alice", "alice@example.com")
pedido = mi_tienda.crear_pedido(cliente)

# Agregar productos al pedido
pedido.agregar_producto(mi_tienda.productos[0], 1)  # Agregar 1 Laptop
pedido.agregar_producto(mi_tienda.productos[1], 2)  # Agregar 2 Mouse

# Mostrar el pedido
print(pedido)

# Listar productos disponibles después del pedido
mi_tienda.listar_productos()

#2 Clase que representa un estudiante
class Estudiante:
    def __init__(self, id_estudiante, nombre):
        self.id_estudiante = id_estudiante  # ID del estudiante
        self.nombre = nombre  # Nombre del estudiante
        self.cursos = []  # Lista de cursos en los que está inscrito

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        cursos_str = ", ".join([curso.nombre for curso in self.cursos])
        return f"Estudiante: {self.nombre} (ID: {self.id_estudiante})\nCursos: {cursos_str}"

# Clase que representa un curso
class Curso:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo  # Código del curso
        self.nombre = nombre  # Nombre del curso
        self.creditos = creditos  # Créditos del curso

    def __str__(self):
        return f"Curso: {self.nombre} (Código: {self.codigo}) - Créditos: {self.creditos}"

# Clase que representa una escuela que gestiona estudiantes y cursos
class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la escuela
        self.estudiantes = []  # Lista de estudiantes
        self.cursos = []  # Lista de cursos

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def listar_estudiantes(self):
        print(f"Estudiantes en {self.nombre}:")
        for estudiante in self.estudiantes:
            print(estudiante)

    def listar_cursos(self):
        print(f"Cursos disponibles en {self.nombre}:")
        for curso in self.cursos:
            print(curso)

# Creación de la escuela y cursos
mi_escuela = Escuela("Escuela POO")

mi_escuela.agregar_curso(Curso(101, "Matemáticas", 4))
mi_escuela.agregar_curso(Curso(102, "Física", 3))
mi_escuela.agregar_curso(Curso(103, "Química", 4))

# Creación de estudiantes
estudiante1 = Estudiante(1, "Carlos Ramirez")
estudiante2 = Estudiante(2, "Luisa Martinez")

# Inscripción de estudiantes en cursos
estudiante1.agregar_curso(mi_escuela.cursos[0])  # Matemáticas
estudiante1.agregar_curso(mi_escuela.cursos[1])  # Física

estudiante2.agregar_curso(mi_escuela.cursos[1])  # Física
estudiante2.agregar_curso(mi_escuela.cursos[2])  # Química

# Agregar estudiantes a la escuela
mi_escuela.agregar_estudiante(estudiante1)
mi_escuela.agregar_estudiante(estudiante2)

# Listar estudiantes y cursos
mi_escuela.listar_estudiantes()
mi_escuela.listar_cursos()
