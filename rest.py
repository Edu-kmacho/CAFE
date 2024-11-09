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

@rest.route('/tabla')
def tabla():

    sqls= 'SELECT * FROM usuarios'
    mysql.execute(sqls)

    result = mysql.fetchall()

    contenidoTabla = []

    for x in result:
        contenidoTabla.append({'id_user':x[0],'id_Nombre':x[1],'id_Telefono':x[2],'id_Diereccion':x[3],'id_Telefono':x[4]})

    if request.method == 'POST':
        
        getid = request.args.get('Nombres')
        up_nombre = request.form['upd_Nombre']
        up_telefono = request.form['upd_Telefono']
        up_direccion = request.form['upd_Direccion']
    return render_template('tabla.html')

if  __name__ == '__main__':
    rest.run()


##esto solo es comentario basura