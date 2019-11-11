from cassandra.cluster import Cluster
import sys
import random as r
import time as t
t.strftime("%I:%M:%S") #Formato de 12 horas


#Nombres
nombres = "G:\\Mi unidad\\TECNOLOGICO DE COLIMA\\9) Semestre\\02 Bases de datos NoSQL\\Unidad 3\\nombres.txt"
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
escritorio = "C:\\Users\\DELL\\Desktop\\tiempos_cassandra.txt"

def conectar_bd():
    try:
        cluster = Cluster(contact_points = ['127.0.0.1'], port = 9042)
        session = cluster.connect()
        session.set_keyspace('proyecto')
        return session
    except ValueError:
        print("No se pudo conectar a BD debido a un error: ")
        print(sys.exc_info()[0])

def nueva_conexion():
    try:
        cluster = Cluster(contact_points = ['127.0.0.1'], port = 9042)
        session = cluster.connect()
        keyspace = 'proyecto'

        rows = session.execute("SELECT keyspace_name FROM system_schema.keyspaces")
        if keyspace in [row[0] for row in rows]:
            session.execute("DROP KEYSPACE "+ keyspace)
        print("Creating keyspace...")
        session.execute("""
            CREATE KEYSPACE proyecto 
            WITH replication = {'class' : 'SimpleStrategy', 'replication_factor':3}
        """)
        session.set_keyspace(keyspace)
        print("Keyspace creada!")
        return session
    except ValueError:
        print('Error en key: ', sys.exc_info()[0])

def crear_tablas(session):
    try:
        session.execute("""
        CREATE TABLE IF NOT EXISTS Alumno(
            id int PRIMARY KEY,
            nombre text
        )
        """)
        session.execute("""
        CREATE TABLE IF NOT EXISTS Materia(
            clave int PRIMARY KEY,
            nombre text,
            id_Alumno int
        )
        """)
        session.execute("""
        CREATE TABLE IF NOT EXISTS Calificaciones(
            id_calif int PRIMARY KEY,
            valor float,
            clave_Materia int,
            id_Alumno int
        )
        """)     
        print("""Tablas
        -Alumno
        -Materia
        -Calificaciones
        Creadas exitosamente!!!""")
    except SystemError as Error:
        print("Error al crear las tablas")
        print(Error)

def llenar_datos(session):
    try:
        
        #insert_alumno = session.prepare("INSERT INTO  Alumno (id, nombre) VALUES (?,?)")
        #insert_materia = session.prepare("""INSERT INTO Materia (clave, nombre, id_alumno) VALUES (?,?,?)""")
        #insert_calificaciones = session.prepare("""INSERT INTO Calificaciones (id_calif, valor, clave_Materia, id_Alumno) VALUES (?, ?,?,?)""")
        
        cantidad = int(input("¿Cuantos datos desea generar?\n(Numero entero): "))
        #batch = BatchStatement()
        tope_batch = 1000
        archivo_nombres = open(nombres, mode="r")
        contador = 0
        contador_interno = 0
        a_alumno = []
        a_nombres= []
        a_materia = []

        #Llenar array de nombres
        for i in archivo_nombres.readlines():
            i = i.rstrip("\n")
            a_nombres.append(i)

        archivo_nombres.close()
        
        print(".:Insertando datos a Alumnos:.")
        #Insertar alumnos
        for _ in range(cantidad):
            id = contador
            if(id not in a_alumno):
                a_alumno.append(id)
            nombre = r.choice(a_nombres)
            #batch.add(insert_alumno, (id, nombre))
            session.execute("""
            INSERT INTO Alumno(id, nombre)
            VALUES(%s, %s)
            """,
            (id, nombre)
            )
            if(contador_interno == tope_batch):
                #session.execute(batch)
                contador_interno = 0
                print("cargando...")
            contador_interno+=1
            contador += 1
        else:
            #session.execute(batch)
            contador_interno = 0
            contador = 0

            

        print(".:Insertando datos a Materias:.")
        #Insertar Materias
        for _ in range(cantidad):
            nombre_materia = r.choice(a_materias)
            alumno = r.choice(a_alumno)
            if(contador not in a_materia):
                a_materia.append(contador)
            #batch.add(insert_materia, (contador, nombre_materia, alumno))
            session.execute("""
            INSERT INTO Materia (clave, nombre, id_alumno)
            VALUES(%s, %s, %s)
            """,
            (contador, nombre_materia, alumno)
            )
            if(contador_interno == tope_batch):            
                #session.execute(batch)
                contador_interno = 0
                print("cargando...")
            contador_interno+=1
            contador += 1
        else:
            #session.execute(batch)
            contador = 0
            contador_interno = 0

        print(".:Insertando datos a Calificaciones:.")
        #Insertar Calificaciones
        for _ in range(cantidad):
            id = contador
            calif = r.random() * 10 
            materia = r.choice(a_materia)
            alumno = r.choice(a_alumno)
            #batch.add(insert_calificaciones, (id, calif, materia, alumno))
            session.execute("""
            INSERT INTO Calificaciones (id_calif, valor, clave_materia, id_alumno)
            VALUES(%s, %s, %s, %s)
            """,
            (id, calif, materia, alumno)
            )
            if (contador_interno == tope_batch):   
                #session.execute(batch)
                contador_interno = 0
                print("cargando...")
            contador_interno+=1
            contador += 1
        else:
            #session.execute(batch)
            contador = 0 
            contador_interno = 0
        
        
        #Escribiendo en archivo que ya se acabaron las inserciones
        archivo_tiempos = open(escritorio, mode="a")
        archivo_tiempos.write("\n"+str(cantidad)+" datos insertados exitosamente\nHora de fin: " + t.strftime("%X"))
        archivo_tiempos.close()
        print("Datos insertados!")
    except SystemError as error:
        print(error)

def mostrar_datos(session):
    
    #Alumnos
    rows_alumnos = session.execute("""
        SELECT * FROM Alumno LIMIT 100;
    """)

    print("\n.:Alumnos:.")
    for row in rows_alumnos:
        print(row.id,"-",row.nombre)

    #Materias
    rows = session.execute("""
        SELECT * FROM Materia LIMIT 100;
    """)
    print("\n.:Materias:.")
    for row in rows:
        print(row.clave,"-", row.nombre)  

    #Calificaciones
    rows_calif = session.execute("""
        SELECT * FROM Calificaciones LIMIT 100;
    """)

    print("\n.:Calificaciones:.")
    for row in rows_calif:
        print(row.id_alumno,"-",row.clave_materia,"-",row.valor)


def main():
    while(True):
        print("""\t\t\t\t\t.:MENU:.
        1.- Conectar a BD\t2.- Crear tablas\t3.-Llenar datos  \t4.-Ver datos\t5.-Crear nueva conexión(Se borra todo)
        \t\t\t\t0.-Salir
        """)
        opc = int(input("Ingrese una opcion entre 0 y 5: "))

        if(opc == 0):
            print("Hasta luego!")
            break
        elif(opc == 1):    
            session = conectar_bd()
        elif(opc == 2):    
            crear_tablas(session)
        elif(opc == 3):
            archivo_tiempos = open(escritorio, mode="w")
            print("Hora de inicio: " + t.strftime("%X"))
            archivo_tiempos.write("Hora de inicio: " + t.strftime("%X"))
            archivo_tiempos.close()
            
            llenar_datos(session)
        elif(opc == 4):
            mostrar_datos(session)
        elif(opc == 5):
            session = nueva_conexion()

if __name__ == '__main__':
    main()