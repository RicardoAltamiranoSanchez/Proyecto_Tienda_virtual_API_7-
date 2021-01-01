from flask import Flask, render_template, request, url_for, session, flash
from database import db
from forms import Usuario_form
import models
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


from flask_migrate import Migrate
from werkzeug.utils import redirect




#################################33


@app.route('/login', methods=['GET', 'POST'])
def Iniciar_Sesion():
    if request.method == 'POST':  # decimos si es metodo es post

        if models.Usuario.query.filter_by(correo=request.form['login_correo']).first() and \
                models.Usuario.query.filter_by(contrasenia=request.form['login_password']).first():
            session['username'] = request.form['login_correo']

            app.logger.info(f'entrando ala consola {request.path}')
            flash('Login Correcto', "exito")
            return redirect(url_for('Bienvenido'))  # volvemos al inicio

            app.logger.info(session['username'])
        else:
            flash('Verifique bien sus credenciales', "error")  # hacemos mensaje flask para decirle que no tien cuenta

    return render_template('Registro.html')

#######
 if request.method=='POST':
           mensaje=request.form['mensaje']
           msg=Message("puto",
                    sender=app.config['MAIL_USERNAME'],
                    recipients="altamiranoricardo546@gmail.com")
           print(msg)
           mail.send(msg)

        flash("Error","error")
        return render_template("contacto.html")
breakpoint()

3333333333333333333##############3
msg = Message(
    subject=f"Mail from {nombre}", body=f"Name:{nombre}E-mail: {correo}+{mensaje}",
    sender=app.config['MAIL_USERNAME'],
    recipients="altamiranoricardo546@gmail.com")
app.logger.info(f'entrando ala consola {request.path}')



























app.config['MAIL_USERNAME']=
app.config['MAIL_PASSWORD']=
,"<h1>no hecho login <h1>

email = request.form['correo']
          token = s.dumps(email, salt='email-confirm')
          msg = Message('Confirmacioin de Correo Electronico', sender=' altamiranoricardo546@gmail.com ',
                      recipients=[email])

          link = url_for('confirm_email', token=token, _external=True)
          msg.body = 'Hola {}{} Este es tu enlace de confirmacion {}'.format(request.form['nombre'],request.form['apellido'],                       link)
          mail.send(msg)

if int(u.nombre.count) < 2:
    flash("Imposible que  tu nombre lleve menos de tres letras", "info")
if int(u.usuario.count) < 4:
    flash("Tu nombre de usuario debe ser creativo", "info")
if int(u.contrasenia.count) < 6:
    flash("Ahora veo por que te hackean", "info")
def Inicio():
    if 'username' in session:#Si el usaurio ya hizo dentro de la session in dentro
        return "<h1>ya hecho login<h1>"
    return "<h1>no hecho login <h1>"















@app.route("/logo.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'img/logo.ico',mimetype='image/vnd.microsof.icon')
#para importar imagens por si me me olvida
< link
rel = "shortcut icon"
herf = " {{url_for('static',filename='img/logo.ico')}}" >
< link
rel = "shortcut icon"
herf = " {{url_for('static',filename='img/logo.ico')}}" >
< img
src = " {{url_for('static',filename='img/logo.ico')}}" >
