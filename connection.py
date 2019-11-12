"""
Program name: connection.py
By: Brandon I. Pérez Sandoval
Description: This program will let you
    make the whole CRUD of a MySQL Database
    housed in Free MySQL Hosting.
Warning: You'll need the library PyMySQL, so if you don't have it use this command
    pip install PyMySQL 
"""
import pymysql
import sys
import random as r
import time as t
t.strftime("%I:%M:%S") #Formato de 12 horas

def connection():
    try:
        db = pymysql.connect("sql9.freemysqlhosting.net","sql9311549","HZWWnleJ9m","sql9311549")
    except:
        print(">>Error en la conexión")
    else:
        print("Conexión exitosa!")
        #Prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Execute SQL query
        cursor.execute("Select VERSION()")
        #Procesing query
        data = cursor.fetchone()
        print("Database version: {0}".format(data))
        return db    
#--------------------------------CRUD--------------------------
def create_tables(db):
    try:
        cursor = db.cursor()
        tablesDatabase = get_tables(db)
        if(len(tablesDatabase) == 0):
            query_alumno = ("""
                CREATE TABLE IF NOT EXISTS Alumno
                (id INT NOT NULL AUTO_INCREMENT, 
                nombre varchar(255) NOT NULL,
                CONSTRAINT id_PK
                PRIMARY KEY(id))
                ENGINE = InnoDB
            """)
            query_materia = ("""
                CREATE TABLE IF NOT EXISTS Materia
                (clave INT NOT NULL AUTO_INCREMENT,
                nombre varchar(255) NOT NULL,                                
                CONSTRAINT clave_PK
                PRIMARY KEY(clave))
                ENGINE = InnoDB
            """)
            query_calificaciones = ("""
                CREATE TABLE IF NOT EXISTS Calificaciones
                (valor float NOT NULL,
                clave_Materia int NOT NULL,
                id_Alumno int NOT NULL,
                CONSTRAINT clave_M_Calif_FK
                FOREIGN KEY(clave_Materia)                
                REFERENCES Materia(clave)
                ON DELETE NO ACTION 
                ON UPDATE NO ACTION,
                CONSTRAINT id_A_Calif_FK
                FOREIGN KEY(id_Alumno)
                REFERENCES Alumno(id)
                ON DELETE NO ACTION 
                ON UPDATE NO ACTION)                
                ENGINE = InnoDB
            """)

            cursor.execute(query_alumno)
            cursor.execute(query_materia)
            cursor.execute(query_calificaciones)
            print("Tablas creadas exitosamente!") 
        else:
            print("Tablas creadas con anterioridad!")
    except:
        db.rollback()
        print(">>Algo salió mal!")           

def show_data(db):
    try:
        cursor = db.cursor()
        tablesDatabase = get_tables(db)
        if(len(tablesDatabase) != 0):
            query_count_alumno = ("SELECT COUNT (id) FROM Alumno;")
            query_count_materia = ("SELECT COUNT (clave) FROM Materia;")
            query_count_calif = ("SELECT COUNT (valor) FROM Calificaciones")

            print("Alumno")
            cursor.execute("SELECT * FROM Alumno LIMIT 10;")
            print("Tiene {0} registros".format(cursor.execute(query_count_alumno))) 
            
            print("Materia")
            cursor.execute("SELECT * FROM Materia LIMIT 10;")
            print("Tiene {0} registros".format(cursor.execute(query_count_materia)))
            
            print("Calificaciones")
            cursor.execute("SELECT * FROM Calificaciones LIMIT 10;")
            print("Tiene {0} registros".format(cursor.execute(query_count_calif)))
        else:
            print("No hay tablas aún!")
    except:
        print(">>Error al mostrar contenido!")
        print(sys.exc_info()[0])

def insert_data(db):
    try:
        cursor = db.cursor()
        tablesDatabase = get_tables(db)
        if(len(tablesDatabase) != 0):            
            n = int(input("¿Cuántos datos desea insertar? "))
            for _ in range(n):

                student_name = r_data(db, 'Alumno')
                query_alumno = ("""INSERT INTO Alumno(id, nombre) 
                    VALUES (NULL,'{0}')"                
                """.format(student_name))
            
            for _ in range(n):                
                subject_name = r_data(db, 'Materia')
                query_materia = ("""INSERT INTO Materia(clave, nombre)
                    VALUES (NULL, '{0}')                
                """.format(subject_name))
            
            for _ in range(n):                
                subject, student, value  = r_data(db, 'Calificacinones')
                query_calificaciones = ("""INSERT INTO Calificaciones(clave_Materia, id_Alumno, valor)
                    VALUES ('{0}','{1}','{2}')
                """.format(subject, student, value))                
    except:
        db.rollback()
        print(">>Error al insertar contenido!")
        print(sys.exc_info()[0])
    else:
        print("Datos insertados!")

def del_data():
    pass

#--------------------------------CRUD--------------------------
#------------------------------HELPERS-------------------------
def get_tables(db):
    cursor = db.cursor()
    tablesDatabase = []
    cursor.execute("SHOW TABLES;")
       
    if cursor:
        tablesDatabase = [
            tablesDatabase.append(table) 
            for table in cursor]

    return tablesDatabase

def drop_tables(db):
    try:        
        cursor = db.cursor()
        
        a = ("ALTER TABLE Materia DROP FOREIGN KEY id_A_Materia_FK;")
        b = ("ALTER TABLE Calificaciones DROP FOREIGN KEY clave_M_Calif_FK;")
        c = ("ALTER TABLE Calificaciones DROP FOREIGN KEY id_A_Calif_FK;")
        cursor.execute(a)
        cursor.execute(b)
        cursor.execute(c)

        d_tables = ("""
            drop table IF EXISTS Calificaciones, Materia, Alumno;                    
        """)
        cursor.execute(d_tables)
    except:
        db.rollback()
        print(">>Error al borrar tablas")
        print(sys.exc_info()[0])
    else:
        print("Tablas borradas!")

def read_data_materias():
    listMaterias = []
    materias = open('materias.txt', 'r')
    for i in materias.readlines():
        if(i != None or i != ""):
            i = i.rstrip("\n")
            listMaterias.append(i)
    return listMaterias

def get_randon_data_materias():
    response = read_data_materias()
    matter = r.choice(response)
    return matter

def r_data(db, table):
    try:
        cursor = db.cursor()

        if(table == 'Alumnos'):
            
            return 
        elif(table == 'Materia'):
            n_subject = get_randon_data_materias()
            return n_subject
        else:
            pass
    except SystemError:
        pass
    else:
        pass
#------------------------------HELPERS-------------------------
#-------------------------------MAIN---------------------------
def main():
    try:
        db = connection()
        while True:
            print("\n.:Menú principal:.")
            opc = int(input("Inserte una opción\n\n\
                1-Crear tablas\t2-Mostrar todos los datos \
                3-Insertar muchos datos\t4-Borrar todos los datos \
                0-Salir\n\n\
                Opción: "))

            if(opc == 0):
                print("Hasta luego!")
                break
            elif(opc == 1):
                print(".:Crear tablas:.")
                create_tables(db)
            elif(opc == 2):
                print(".:Mostrar todos los datos:.")
                show_data(db)
            elif(opc == 3):
                print(".:Insertar muchos datos:.")
                #insert_data(db)
            elif(opc == 4):
                print(".:Borrar todos los datos:.")
            elif(opc == 404):
                drop_tables(db)
            else:
                print("Opción incorrecta, intente de nuevo!")
    except:
        print(">>Error")
    finally:
        db.close()

if __name__ == '__main__':
    main()
