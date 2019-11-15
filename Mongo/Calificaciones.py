class Calificaciones:

    def __init__(self, valor, clave_Materia, id_Alumno):
        self.valor = valor
        self.clave_Materia = clave_Materia
        self.id_Alumno = id_Alumno

    def toDBCollection (self):
        return {
            "valor":self.valor,
            "clave_Materia":self.clave_Materia,
            "id_Alumno":self.id_Alumno
        }

    def __str__(self):
        return "valor: %i - clave_Materia: %i - id_Alumno: %i" \
               %(self.valor, self.clave_Materia, self.id_Alumno)
