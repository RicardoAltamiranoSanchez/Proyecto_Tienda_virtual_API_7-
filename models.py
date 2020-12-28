#Crear clase modelo
import app
from werkzeug.security import generate_password_hash
import datetime

class Usuario(app.db.Model):#Creamo la clase modelo para la base de datos funcion model
    id=app.db.Column(app.db.Integer, primary_key=True)#para crear las columnas en la base de datos
    nombre=app.db.Column(app.db.String(255))
    apellido=app.db.Column(app.db.String(255))
    correo=app.db.Column(app.db.String(255))
    usuario=app.db.Column(app.db.String(255))
    contrasenia=app.db.Column(app.db.String(255))
    hora_registro=app.db.Column(app.db.DateTime, default=datetime.datetime.now)
    def __init__(self,nombre,apellido,correo,usuario,contrasenia):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.usuario=usuario
        self.contrasenia=self.__create_password(contrasenia)
    def __str__(self):
        return(
               f'Id:{self.id},'
               f'Nombre:{self.nombre},'
               f'Apellido:{self.apellido},'
               f'Email:{self.correo},'
               f'Usuario:{self.usuario},'
               f'Contraseña:{self.contrasenia}')
    def __create_password(self,contrasenia):
        return generate_password_hash(contrasenia)