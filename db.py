import mysql.connector
from mysql.connector import Error


def connectar():
    conexion = None
    try:
        conexion = mysql.connector.connect(host="localhost",user="root",password="",database="hospital")
    except Error as e:
        print("Failed to connect: "+e)

"""
def connectar():
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
    cursor.execute("SELECT * FROM usuarios")
    fila = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas
"""