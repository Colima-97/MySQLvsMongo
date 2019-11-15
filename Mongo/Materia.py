class Materia:

    def __init__(self, clave, nombre):
        self.clave = clave
        self.nombre = nombre

    def toDBCollection (self):
        return {
            "clave":self.clave,
            "nombre":self.nombre
        }

    def __str__(self):
        return "clave: %i - nombre: %s" \
               %(self.clave, self.nombre)
