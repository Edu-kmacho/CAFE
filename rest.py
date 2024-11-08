from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mysqlcon


#Hola Erick, si esto funciona lloro
dbconect = mysqlcon.connect(host="localhost",user="root", password="",database="restaurante_ing")

mysql = dbconect.cursor()

rest = Flask(__name__)


@rest.route('/')
def index():
   
    return render_template('index.html')

@rest.route('/desayunos')
def desayunos():


    return render_template('desayunos.html')

@rest.route('/comida')
def comida():
    return render_template('comida.html')

@rest.route('/postres')
def postres():
    return render_template('postres.html')

@rest.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')

@rest.route('/carrito')
def carrito():
    return render_template('carrito.html')

@rest.route('/crud', methods =['GET','POST'])
def crud():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Direccion = request.form['Direccion']
        Numero = request.form['Numero']

        sql = "INSERT INTO usuarios(Nombre,Direccion,Numero) VALUES(%s,%s,%s)"
        values = (Nombre, Direccion, Numero)

        mysql.execute(sql, values)
        dbconect.commit()

        return "Usuario agregado con exito <a href='/crud'>volver</a>"
    else:
        return render_template('crud.html')

@rest.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

if  __name__ == '__main__':
    rest.run()


##esto solo es comentario basura