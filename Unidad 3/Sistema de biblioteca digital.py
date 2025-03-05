class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Utiliza una tupla para almacenar el autor y el título, ya que estos no cambiarán una vez creados.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Cada usuario tiene un ID único y una lista de libros prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase que gestiona la biblioteca digital.
    Contiene colecciones de libros, usuarios y préstamos.
    """
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para IDs de usuarios únicos
        self.usuarios = {}  # Diccionario para almacenar objetos Usuario por ID

    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.
        """
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")

    def quitar_libro(self, isbn):
        """
        Quita un libro de la biblioteca.
        """
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} quitado correctamente.")
        else:
            print(f"Libro con ISBN {isbn} no encontrado en la biblioteca.")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.
        """
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def dar_de_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario de la biblioteca.
        """
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro a un usuario.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        if isbn not in self.libros_disponibles:
            print(f"Libro con ISBN {isbn} no disponible.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.libros_prestados.append(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        """
        Devuelve un libro prestado por un usuario.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_devuelto = None

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_devuelto = libro
                break

        if libro_devuelto:
            usuario.libros_prestados.remove(libro_devuelto)
            self.libros_disponibles[isbn] = libro_devuelto
            print(f"Libro '{libro_devuelto.titulo_autor[0]}' devuelto por {usuario.nombre}.")
        else:
            print(f"Libro con ISBN {isbn} no encontrado en los préstamos de {usuario.nombre}.")

    def buscar_libros(self, criterio, valor):
        """
        Busca libros por título, autor o categoría.
        """
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print(f"Resultados de búsqueda para {criterio} '{valor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        """
        Lista todos los libros prestados a un usuario.
        """
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-0307350487")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0451524935")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("Ana Gómez", "002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("001", "978-0307350487")
    biblioteca.prestar_libro("002", "978-0451524935")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")
    biblioteca.listar_libros_prestados("002")

    # Devolver libros
    biblioteca.devolver_libro("001", "978-0307350487")
    biblioteca.devolver_libro("002", "978-0451524935")

    # Buscar libros
    biblioteca.buscar_libros("autor", "Gabriel García Márquez")
    biblioteca.buscar_libros("categoria", "Ciencia Ficción")

    # Dar de baja usuario
    biblioteca.dar_de_baja_usuario("001")