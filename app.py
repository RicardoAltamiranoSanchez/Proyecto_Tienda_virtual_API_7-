import os

import jinja2
from flask import Flask, render_template, request, url_for, session, flash, jsonify, send_from_directory
from database import db
from forms import Usuario_form,Frutas_form
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
PASS_DB='riki'
URL_DB='localhost'
NAME_DB='tienda3b2'
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
@app.route('/')
def Inicio():
    return render_template('index.html')

@app.route('/Registro', methods=['GET', 'POST'])
def Registro():
    total_usuario = models.Usuario.query.count()
    if request.method=='POST':
            if models.Usuario.query.filter_by(correo=request.form['correo']).first() is None:
                if models.Usuario.query.filter_by(contrasenia=request.form['password']).first() is None:
                    email = request.form['correo']
                    token = s.dumps(email, salt='email-confirm')
                    msg = Message('Confirmacioin de Correo Electronico', sender=' altamiranoricardo546@gmail.com ',
                                  recipients=[email])

                    link = url_for('confirm_email', token=token, _external=True)
                    msg.body = 'Hola {}{} Este es tu enlace de confirmacion {}'.format(request.form['nombre'],
                                                                                       request.form['apellido'], link)
                    mail.send(msg)
                    return '<h1> Revise su bandeja de entrada de su correo para confirmacion</h1>'
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
           return '<h1>Tu token ya expiro!</h1>'
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
      return '<h1> token confirmado <h1>'

@app.route('/Salir',methods=['GET','POST'])
def Salir():
    if request.method=='POST':

       comentario=models.Evaluacion(usuario_id=session['id'],
                                    comentario=request.form['comentario'])
       app.logger.info(f'Informacion de salida{request.path}')
       app.logger.info(f'Informacion de salida{comentario}')
       db.session.add(comentario)
       db.session.commit()
       session.pop('nombre')
       return redirect(url_for('Inicio'))
    return render_template('Salir.html')
@app.route('/Bienvenido')
def Bienvenido():
    pass
    return render_template('bienvenido.html')

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
        #return redirect(url_for("Inicio"))
        #return ("contacto.html")

    return render_template('contacto.html')
@app.route('/Casa')
def Casa():
    return render_template('home.html')
@app.route('/Demo')
def Demo():
    return render_template('demo.html')

@app.route('/Frutas')
def Frutas():
    return render_template('frutas.html')
@app.route('/Enlatados')
def Enlatados():
    return render_template('demo_enlatados.html')

@app.route('/Botanas')
def Botanas():
    return render_template('demo_botanas.html')
@app.route('/Refrescos')
def Refrescos():
    return render_template('demo_refrescos.html')

@app.route('/Licores')
def Licores():
    return render_template('demo_licores.html')
@app.route('/Portafolio')
def Portafolio():
    return render_template('portafolio.html')
@app.route('/session')

@app.route('/Base')
def Base():
    if 'nombre' in session:  # Si el usaurio ya hizo dentro de la session in dentro
        nombre2 = session['nombre']
        apellido2 = session['apellido']
        return render_template('base_usuario.html', nombre=nombre2, apellido=apellido2)
@app.route('/Cliente')
def Usuario_index():
    if 'nombre' in session:  # Si el usaurio ya hizo dentro de la session in dentro
        nombre = session['nombre']
        apellido = session['apellido']

        return render_template('usuario_index.html', nombre=nombre, apellido=apellido)
    mensaje = flash("Debes Iniciar Sesion primeroo", "error")
    return redirect(url_for('Inicio'))
@app.route('/Cliente_Casa')
def Usuario_home():

    return render_template('usuario_home.html')

@app.route('/Cliente_Contacto',methods=['GET','POST'],)
def Usuario_contacto():
    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        msg = Message(subject=f"Sunburts Contactame:{nombre}", body=f"Nombre:{nombre}\nCorreo: {correo}\n\n\n{mensaje}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        app.logger.info(msg)
        mail.send(msg)
        flash("Mensaje enviado con exito", "mensaje")

        return redirect(url_for('Usuario_index'))
    else:
        flash("No se puedo enviar el correo", "error")
        # return redirect(url_for("Inicio"))
        # return ("contacto.html")
    return render_template('usuario_contacto.html')

@app.route('/Venta_base')
def Venta():
    return render_template('venta_base.html')
@app.route('/Venta_Enlatados')
def Ventas_enlatados():
    return  render_template('macro_cliente_enlatados.html')
@app.route('/Venta_Botonas',methods=['GET','POST'])
def Ventas_botanas():
    if request.method=='POST':
        papa=request.form['papas']
        print(papa)
        app.logger.info(f'entrando ala consola {request.path}')

    return  render_template('macro_cliente_botanas.html')
@app.route('/Venta_Refrescos')
def Ventas_refrescos():
    return  render_template('macro_cliente_refrescos.html')
@app.route('/Venta_Licores')
def Ventas_licores():
    return  render_template('macro_cliente_licores.html')
#Aqui va la ventas no pude separarlo daba errores
@app.route('/Venta_frutas',methods=['GET','POST'])
def Ventas_frutas():
    #No es bueno hacer el codigo asi por el momemto lo hare asi con el for no salel deacuero
    fruta1=models.Frutas.query.filter_by(id=1).first()
    fruta2=models.Frutas.query.filter_by(id=2).first()
    fruta3=models.Frutas.query.filter_by(id=3).first()
    fruta4=models.Frutas.query.filter_by(id=4).first()
    fruta5=models.Frutas.query.filter_by(id=5).first()
    fruta6=models.Frutas.query.filter_by(id=6).first()
    fruta7=models.Frutas.query.filter_by(id=7).first()
    fruta8=models.Frutas.query.filter_by(id=8).first()
    fruta9=models.Frutas.query.filter_by(id=9).first()
    fruta10=models.Frutas.query.filter_by(id=10).first()
    fruta11=models.Frutas.query.filter_by(id=11).first()
    fruta12=models.Frutas.query.filter_by(id=12).first()
    fruta13=models.Frutas.query.filter_by(id=13).first()
    fruta14=models.Frutas.query.filter_by(id=14).first()
    fruta15=models.Frutas.query.filter_by(id=15).first()
    fruta16=models.Frutas.query.filter_by(id=16).first()

    venta_form=Frutas_form(obj=fruta1)  # asociamos nuestra base de datos a  nuesta clase form o formulario
    if request.method == 'POST':  # preguntamos si el tipo de metodo es de tipo post importamos del objeto flask.request
        if venta_form.validate_on_submit():  # preguntamos si el formulario si es valido solo si se hace elenvio del formulario
            venta_form.populate_obj(fruta1)  # llenamos el objetos que persona que definimos de clase models
            app.logger.debug(f'Persona a insertar {fruta1}')

            lista= models.Listado(cliente_id=session['id'],
                                  nombre_cliente=session['nombre'],
                                  frutas_id=fruta1.id,
                                  nombre=fruta1.nombre,
                                  cantidad=fruta1.cantidad,
                                  costo=fruta1.costo)

            db.session.add(lista)
            db.session.commit()
    venta_form=Frutas_form(obj=fruta2)  # asociamos nuestra base de datos a  nuesta clase form o formulario
    if request.method == 'POST':  # preguntamos si el tipo de metodo es de tipo post importamos del objeto flask.request
        if venta_form.validate_on_submit():  # preguntamos si el formulario si es valido solo si se hace elenvio del formulario
            venta_form.populate_obj(fruta2)  # llenamos el objetos que persona que definimos de clase models
            app.logger.debug(f'Persona a insertar {fruta2}')


            lista= models.Listado(cliente_id=session['id'],
                                  nombre_cliente=session['nombre'],
                                  frutas_id=fruta2.id,
                                  nombre=fruta2.nombre,
                                  cantidad=fruta2.cantidad,
                                  costo=fruta2.costo)

            db.session.add(lista)
            db.session.commit()


    return  render_template('macro_cliente_fruta.html',fruta1=fruta1,fruta2=fruta2,fruta3=fruta3,fruta4=fruta4,fruta5=fruta5,
                            fruta6=fruta6,fruta7=fruta7,fruta8=fruta8,fruta9=fruta9,fruta10=fruta10,fruta11=fruta11,
                            fruta12=fruta12,fruta13=fruta13,fruta14=fruta14,fruta15=fruta15,fruta16=fruta16,venta=venta_form)
@app.route('/Listado')
def Listado():

     return render_template('listado.html')
@app.route('/Repartidores',methods=['GET','POST'])
def Repartidores():
    repatidor = models.Usuario_Repatidor.query.filter_by(id=1).first()
    session['nombre_repartidor'] = repatidor.nombre
    session['apellido_repartidor'] = repatidor.apellido
    session['id_repartidor'] = repatidor.id
    app.logger.info(f'entrando ala consola {request.path}')
    nombre=session['nombre_repartidor']
    apellido=session['apellido_repartidor']
    return render_template('repartidores.html',nombre=nombre,apellido=apellido)
@app.route('/Pedidos')
def Pedidos():
    return render_template('pedidos.html')
@app.route('/pendientes')
def Pendientes():
    return render_template('pendientes.html')
@app.route('/administracion')
def Administracion():
    nombre = session['nombre_administrador']
    apellido = session['apellido_administrador']
    return render_template('administracion.html',nombre=nombre,apellido=apellido)
@app.route('/Estado_Envio')
def Estado_envio():
    return render_template('Estado_envio.html')
@app.route('/Administracion_ingresos')
def Admin_ingresos():
    return render_template('admin_ingresos.html')
@app.route('/registro_financiero')
def Registro_financiero():
    return render_template('registro_financiero_admin.html')
@app.route('/Registro_envios')
def Registro_envios():
    return render_template('registro_envios_admin.html')
@app.route('/Lista_productos')
def Lista_productos():
    return render_template('lista_productos_admin.html')
@app.route('/Pago',methods=['GET','POST'])
def Pago():
    return  render_template('pago.html')
@app.errorhandler(404)
def Pagina_no_encontrada(e):
    return render_template('404.html'),404


if __name__=='__main__':

    app.run(debug=True,port=8000,host=0000)


