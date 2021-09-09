from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registra')
def registra():
    return render_template('registra.html')

@app.route('/procesa',methods=['POST'])
def procesa():
    return 'vamos'

if __name__ == '__main__':
   app.run(debug = True)