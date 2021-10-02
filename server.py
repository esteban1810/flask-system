from flask import Flask, render_template, request, redirect
from usuario import Usuario
from db import conectar, getListadoPersonas, guardarUsuario, getListadoEnfermedades

usuarios = []

app = Flask(__name__)


@app.route('/')
def root():
    conectar()
    return redirect('/login')


@app.route('/listado')
def listado():
    conexion = conectar()
    if conexion == None:
        return "<p>Error de conexion...</p>"
    else:
        listado = getListadoPersonas(conexion)
        return render_template("listado.html",listado=listado)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/loguearse',methods=['POST'])
def loguearse():
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    for usuario in usuarios:
        if usuario.getContrasenia() == contrasenia:
            if usuario.getCorreo() == correo:
                return redirect('/home')
    return redirect('/login')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registra')
def registra():
    return render_template('registra.html')

@app.route('/procesa',methods=['POST'])
def procesa():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    genero = request.form['genero']
    tipo = request.form['tipo']
    cedula = request.form['cedula']
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    conexion = conectar()
    guardarUsuario(conexion,nombre,apellidos,genero,tipo,cedula,correo,contrasenia)
    return redirect('/home')

@app.route('/enfermadades')
def enfermadades():
    conexion = conectar()
    if conexion == None:
        return "<p>Error de conexion...</p>"
    else:
        enfermadades = getListadoEnfermedades(conexion)
        return render_template("enfermedades.html",enfermadades=enfermadades)

def bucleFor():
    cadena = ""
    for user in usuarios:
        cadena+=user.toString()
    return cadena

if __name__ == '__main__':
   app.run(debug = True)