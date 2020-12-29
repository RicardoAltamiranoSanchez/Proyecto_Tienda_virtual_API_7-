import os

import jinja2
from flask import Flask, render_template, request, url_for, session, flash,jsonify
from database import db
from forms import Usuario_form
import models
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from Login import login

from flask_migrate import Migrate
from werkzeug.utils import redirect
app=Flask(__name__)
#jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
#template=jinja_env.get_template('content.html')
#template.render('index.html')
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
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER', '2020sunburst.systems@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS', 'septimogrado')
app.config['MAIL_PORT']=587
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS']=True
mail = Mail(app)
app.register_blueprint(login)

@app.route('/')#es un decorador para pedemor a donde vamos a envira la inforamcion
def Inicio():
    return render_template('macro_navegador.html')
@app.route('/Registro', methods=['GET', 'POST'])
def Registro():
    total_usuario = models.Usuario.query.count()
    if request.method=='POST':
            if models.Usuario.query.filter_by(correo=request.form['correo']).first() is None:
                if models.Usuario.query.filter_by(contrasenia=request.form['usuario']).first() is None:

                            u = models.Usuario(nombre=request.form['nombre'],
                                      apellido=request.form['apellido'],
                                      correo=request.form['correo'],
                                      usuario=request.form['usuario'],
                                      contrasenia=request.form['password'], )
                            app.logger.info(f'entrando ala consola {request.path}')
                            db.session.add(u)
                            db.session.commit()
                            flash("Registro Exitoso", "exito")
                            app.logger.info(f'entrando ala consola {request.path}')
                            return redirect(url_for("Registro"))

                else:
                     flash(f"Nombre de usuario ocupado {request.form['usuario']}", "info")

            else:
                flash(f"Ya tienes una cuenta con este correo {request.form['correo']}","info")
    return render_template('Registro.html',total_usuario=total_usuario)


@app.route('/confirm_email/<token>')
def confirm_email(token):

      try:
         email= s.loads(token, salt='email-confirm', max_age=3600)
      except SignatureExpired:
           return '<h1>Tu Token expiro!</h1>'
      return'<h1>Token confirmado!</h1>'

@app.route('/Salir')
def logout():
    session.pop('username')
    return redirect(url_for('Inicio'))
@app.route('/Bienvenido')
def Bienvenido():
    pass
    return render_template('bienvenido.html')
@app.route('/Menu')
def Menu():
    if 'username' in session:  # Si el usaurio ya hizo dentro de la session in dentro
        flash(f"Bienvenido ", "bienvenido")
        return render_template('menu.html')
    mensaje=flash("Debes Iniciar Sesion primeroo","error")
    return redirect(url_for('Inicio',mensaje))
@app.route('/Contacto',methods=['GET','POST'])
def Contacto():
    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        msg = Message( subject=f"Sunburts Contactame:{nombre}", body=f"Nombre:{nombre}\nCorreo: {correo}\n\n\n{mensaje}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']])
        app.logger.info(msg)
        mail.send(msg)
        flash("Mensaje enviado con exito", "mensaje")


        return redirect(url_for("Inicio"))
    else:
        flash("No se puedo enviar el correo", "error")
        return redirect(url_for("Inicio"))
    return ("contacto.html")

    return render_template('contacto.html')
@app.errorhandler(404)
def Pagina_no_encontrada(e):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run(debug=True,port=5000,host=0000)


