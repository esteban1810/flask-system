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


def validarUsuario(conexion,correo,contrasenia):
    cursor = conexion.cursor()
    sql = "SELECT * FROM usuarios WHERE correo=%s AND contrasenia=%s"
    args = (correo,contrasenia)
    cursor.execute(sql,args)
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    try:
        return filas[0]
    except:
        return None


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

def guardarUsuario(conexion,correo,nombre,apellidos,genero,cedula,contrasenia,tipo):
    exito=False
    cursor = conexion.cursor()
    sql = "INSERT INTO usuarios VALUES (%s,%s,%s,%s,%s,%s,%s)"
    listado = (correo,nombre,apellidos,genero,cedula,contrasenia,tipo)
    cursor.execute(sql,listado)
    conexion.commit()
    cursor.close()
    conexion.close()
    return True