import mysql.connector
from mysql.connector import Error


def conectar():
    conexion = None
    try:
        conexion = mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
        if conexion.is_connected():
            print("Connected")
            return conexion
        else:
            return None
    except Error as e:
        print("Failed to connect: "+e)


def getListadoPersonas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT correo,contrasenia FROM usuarios")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas

def getListadoEnfermedades(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM enfermedades")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas

# def getListadoPersonas(conexion):
#     cursor = conexion.cursor()
#     cursor.execute("SELECT correo,contrasenia FROM usuarios")
#     filas = cursor.fetchall()
#     cursor.close()
#     conexion.close()
#     return filas


def guardarUsuario(conexion,nombre,apellidos,genero,tipo,cedula,correo,contrasenia):
    exito=False
    cursor = conexion.cursor()
    sql = "INSERT INTO usuarios VALUES (%s,%s,%s,%s,%s,%s,%s)"
    listado = (nombre,apellidos,genero,tipo,cedula,correo,contrasenia)
    cursor.execute(sql,listado)
    conexion.commit()
    cursor.close()
    conexion.close()
    return True