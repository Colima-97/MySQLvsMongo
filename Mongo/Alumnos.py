class Alumnos:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def toDBCollection (self):
        return {
            "id":self.id,
            "nombre":self.nombre
        }

    def __str__(self):
        return "id: %i - Nombre: %s" \
               %(self.id, self.nombre)
