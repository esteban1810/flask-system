from flask import Flask, render_template, request, redirect
from usuario import Usuario

usuarios = []

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loguearse',methods=['POST'])
def loguearse():
    for usuario in usuarios:
        if usuario.correo = correo:
            if usuario.contrasenia = contrasenia:
                return redirect('/home')


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
    cedula = request.form['cedula']
    correo = request.form['correo']
    contrasenia = request.form['contrasenia']
    usuario = Usuario(nombre,apellidos,genero,cedula,correo,contrasenia)
    usuarios.append(usuario)
    return bucleFor()

def bucleFor():
    cadena = ""
    for user in usuarios:
        cadena+=user.toString()
    return cadena

if __name__ == '__main__':
   app.run(debug = True)