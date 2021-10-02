from flask import Flask, render_template, request, redirect
from usuario import Usuario
from db import *

app = Flask(__name__)

user = None


@app.route('/')
def root():
    return redirect('/login')


@app.route('/listado')
def listado():
    global user
    if(user == None):
        return render_template('login.html')
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
    global user
    conexion = conectar()
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    user = validarUsuario(conexion,correo,contrasenia)
    if(user != None):
        return redirect('/home')
    return redirect('/login')

@app.route('/home')
def home():
    global user
    if(user != None):
        return render_template('home.html')
    return render_template('login.html')
        

@app.route('/registra')
def registra():
    return render_template('registra.html')

@app.route('/procesa',methods=['POST'])
def procesa():
    global user
    if(user == None):
        return render_template('login.html')

    return render_template('login.html')
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    genero = request.form['genero']
    tipo = request.form['tipo']
    cedula = request.form['cedula']
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    conexion = conectar()
    guardarUsuario(conexion,correo,nombre,apellidos,genero,cedula,contrasenia,tipo)
    return redirect('/home')

@app.route('/enfermadades')
def enfermadades():
    global user
    if(user == None):
        return render_template('login.html')

    conexion = conectar()
    if conexion == None:
        return "<p>Error de conexion...</p>"
    else:
        enfermadades = getListadoEnfermedades(conexion)
        return render_template("enfermedades.html",enfermadades=enfermadades)

if __name__ == '__main__':
   app.run(debug = True)