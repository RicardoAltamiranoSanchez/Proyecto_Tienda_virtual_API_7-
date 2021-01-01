import flask
from flask import Flask, render_template, request, url_for, session, flash,jsonify
from database import db
from forms import Usuario_form
import models
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


from flask_migrate import Migrate
from werkzeug.utils import redirect
app=Flask(__name__)

app.config.from_object(__name__)
#Configuracion para la macros de datos
USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='Tienda3B2'
FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'#CADENA DE CONEXION COMPLETA
app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB#cual es laconexion de la bd que va utilizar
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)

#Configuracion de flak-wtf osa el form




s = URLSafeTimedSerializer('Thisisasecret!')

app.config['SECRET_KEY']='llave_maestra'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_USERNAME']='altamiranoricardo546@gmail.com'
app.config['MAIL_PASSWORD']="Ricardo.1993linux"
app.config['MAIL_PORT']=587
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS']=True
mail = Mail(app)

login=flask.Blueprint('login',__name__)

@login.route('/Login', methods=['GET', 'POST'])
def Iniciar_Sesion():
    total_usuario = models.Usuario.query.count()
    if request.method == 'POST':  # decimos si es metodo es post

        if models.Usuario.query.filter_by(correo=request.form['login_correo']).first() and \
                models.Usuario.query.filter_by(contrasenia=request.form['login_password']).first():
            usuario = request.form['login_correo']  # obtenemos la informacion del form registrada con corchetes de array
            session['username'] = usuario
            app.logger.info(f'entrando ala consola {request.path}')
            flash('Login Correcto', "exito")
            return redirect(url_for('Bienvenido'))  # volvemos al inicio

            app.logger.info(session['username'])
        else:
            flash('Verifique bien sus credenciales', "error")  # hacemos mensaje flask para decirle que no tien cuenta

    return render_template('Login.html',total_usuario=total_usuario)
