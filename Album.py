class Album:
    def __init__(self, id, nombre, fecha_publicacion):
        self.id = id
        self.nombre = nombre
        self.fecha_publicacion = fecha_publicacion
        self.canciones = []