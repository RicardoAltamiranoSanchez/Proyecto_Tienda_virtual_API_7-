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

    return render_template('base.html')

