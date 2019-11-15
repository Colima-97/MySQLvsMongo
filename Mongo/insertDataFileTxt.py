a_materias = ["Calculo diferencial", "Fundamentos de programacion","Taller de etica",
    "Matematicas discretas","Taller de administracion","Fundamentos de investigacion",
    "Calculo integral","POO","Contabilidad financiera","Quimica","Algebra lineal","Probabilidad",
    "Calculo vectorial","Estructura de datos","Cultura empresarial","IO","Desarrollo sustentable","Fisica",
    "Ecuaciones diferenciales","Metodos numericos","TAP","Fundamentos de bases de datos","Simulacion","Principos electricos",
    "Graficacion","Fundamentos de telecomunicaciones","Sistemas operativos","Taller de base de datos","Fundamentos de ingenieria de software",
    "Arquitectura de computadoras","Lenguajes y automatas 1", "Redes de computadoras","Taller de sistemas operativos","Administracion de bases de datos",
    "Ingenieria de software","Lenguajes de interfaz","Lenguajes y automatas 2","Conmutacion y enrutamiento de redes","Taller de investigacion 1",
    "Gestion de proyectos de software","Sistemas programables","Programacion logica y funcional","Administracion de redes","Taller de investigacion 2",
    "Programacion web","Inteligencia artifical","Programacion Python","Bases de datos NoSQL"]

def insert_materias():
    materias = open('materias.txt', 'w')
    for i in a_materias:
        materias.write(i + '\n')
    materias.close()

def main():
    insert_materias()

if __name__ == "__main__":
    main()