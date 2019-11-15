#Librería Conexion
from pymongo import MongoClient
import sys
from Alumnos import Alumnos
from Materia import Materia
from Calificaciones import Calificaciones


nombres = 'nombres.txt'
materiasTxt = 'materias.txt'
# Cantidad de registros a guardar
cantidad_registros = 5000

registrarA = []
contRA = 1
while(contRA<cantidad_registros):
    archivo_nombres = open(nombres, mode="r", encoding="utf8")
    for i in archivo_nombres.readlines():
        i = i.rstrip("\n")
        registrarA.append(Alumnos(contRA,i))
        print('Creando registros de alumnos: ', contRA)
        contRA = contRA + 1
    archivo_nombres.close()

registrarMa = []
contMa = 1
try:
    while(contMa<cantidad_registros):
        materias = open(materiasTxt, mode = 'r', encoding='UTF-8')
        for i in materias.readlines():
            if(i != None or i != ""):
                i = i.rstrip("\n")            
                registrarMa.append(Materia(contMa,i))
                print('Creando registros de materia: ', contMa)
                contMa = contMa + 1
        materias.close()
except:
    print(">>Error con el archivo")
    print(sys.exc_info()[0])

registrarCal = []
for i in range(cantidad_registros):
    registrarCal.append(Calificaciones(70,registrarMa[i].clave,registrarA[i].id))
    print('Creando registros de calificaciones: ', i)

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# PASO 2: Conexión a la base de datos
db = mongoClient.NoSQL


# PASO 3: Obtenemos una coleccion para trabajar con ella
collectA = db.Alumnos
collectMa = db.Materia
collectCal = db.Calificaciones


# PASO 4.1: "CREATE"
contA = 1
for Alumnos in registrarA:
    collectA.insert_one(Alumnos.toDBCollection())
    print('Guardado registro de Alumno: ',contA)
    contA = contA + 1

contMa = 1
for Materia in registrarMa:
    collectMa.insert_one(Materia.toDBCollection())
    print('Guardado registro de Materia: ',contMa)
    contMa = contMa + 1

contCal = 1
for Calificaciones in registrarCal:
    collectCal.insert_one(Calificaciones.toDBCollection())
    print('Guardado registro de Calificaciones: ',contCal)
    contCal = contCal + 1
