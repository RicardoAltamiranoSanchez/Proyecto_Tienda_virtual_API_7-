#Crear clase modelo
import app
from werkzeug.security import generate_password_hash
import datetime
from app import db

class Usuario(app.db.Model):#Creamo la clase modelo para la macros de datos funcion model
    id=app.db.Column(app.db.Integer, primary_key=True)#para crear las columnas en la macros de datos
    nombre=app.db.Column(app.db.String(255))
    apellido=app.db.Column(app.db.String(255))
    correo=app.db.Column(app.db.String(255))
    usuario=app.db.Column(app.db.String(255))
    contrasenia=app.db.Column(app.db.String(255))
    evaluacion=app.db.relationship('Evaluacion')
    listado=app.db.relationship('Listado')
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
class Usuario_Repatidor(app.db.Model):#Creamo la clase modelo para la macros de datos funcion model
    id=app.db.Column(app.db.Integer, primary_key=True)#para crear las columnas en la macros de datos
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
class Administracion(app.db.Model):#Creamo la clase modelo para la macros de datos funcion model
    id=app.db.Column(app.db.Integer, primary_key=True)#para crear las columnas en la macros de datos
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
class Evaluacion(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
    usuario_id=app.db.Column(app.db.Integer,app.db.ForeignKey('usuario.id'))
    comentario=app.db.Column(app.db.Text())
    hora_Salida=app.db.Column(app.db.DateTime, default=datetime.datetime.now)


    def __init__(self,usuario_id,comentario):
        self.usuario_id=usuario_id
        self.comentario=comentario

    def __str__(self):
        return(
               f'Id:{self.id},'
               f'Nombre:{self.usuario_id},'
               f'Apellido:{self.comentario},'
               )

class Producto(app.db.Model):#Creamo la clase modelo para la macros de datos funcion model
    id=app.db.Column(app.db.Integer, primary_key=True)#para crear las columnas en la macros de datos
    frutas=app.db.relationship('Frutas')
    tipo=app.db.Column(app.db.String(255))
    fruta=app.db.relationship('Frutas')
    enlatados=app.db.relationship('Enlatados')
    botanas=app.db.relationship('Botanas')
    refrescos=app.db.relationship('Refrescos')
    licores=app.db.relationship('Licores')


    def __init__(self,tipo):
        self.tipo=tipo
    def __str__(self):
        return(
               f'Id:{self.id},'
               f'Tipo:{self.tipo},'
               )
class Frutas(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        producto_id = app.db.Column(app.db.Integer, app.db.ForeignKey('producto.id'))
        nombre = app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)
        imagen=app.db.Column(app.db.String(255))

        def __init__(self, nombre,costo,imagen):
            self.nombre = nombre
            self.costo = costo
            self.imagen=imagen

        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.nombre},'
                f'Costo:{self.costo,}',
                f'Imagen:{self.imagen}')
class Listado(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        cliente_id=app.db.Column(app.db.Integer,app.db.ForeignKey('usuario.id'))
        nombre_cliente=app.db.Column(app.db.String(255))
        frutas_id = app.db.Column(app.db.Integer, app.db.ForeignKey('frutas.id'))
        nombre=app.db.Column(app.db.String(255))
        cantidad= app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)

        def __init__(self,cliente_id,nombre_cliente,frutas_id,nombre,cantidad,costo):
            self.cliente_id =cliente_id
            self.nombre_cliente =nombre_cliente
            self.frutas_id =frutas_id
            self.nombre=nombre
            self.cantidad=cantidad
            self.costo=costo

        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.cliente_id},'
                f'Nombre:{self.nombre_cliente},'
                f'Nombre:{self.frutas_id},'
                f'Nombre:{self.nombre,}'
                f'Nombre:{self.cantidad,}'
                f'Nombre:{self.costo,}')
class Enlatados(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        producto_id = app.db.Column(app.db.Integer, app.db.ForeignKey('producto.id'))
        nombre = app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)
        imagen=app.db.Column(app.db.String(255))


        def __init__(self, nombre,costo,imagen):
            self.nombre = nombre
            self.costo = costo
            self.imagen=imagen


        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.nombre},'
                f'Costo:{self.costo,},'
                f'Imagen:{self.imagen}')
class Botanas(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        producto_id = app.db.Column(app.db.Integer, app.db.ForeignKey('producto.id'))
        nombre = app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)
        imagen=app.db.Column(app.db.String(255))
        def __init__(self, nombre,costo,imagen):
            self.nombre = nombre
            self.costo = costo
            self.imagen=imagen

        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.nombre},'
                f'Costo:{self.costo,},'
                f'Imagen:{self.imagen}')

class Refrescos(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        producto_id = app.db.Column(app.db.Integer, app.db.ForeignKey('producto.id'))
        nombre = app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)
        imagen=app.db.Column(app.db.String(255))
        def __init__(self, nombre,costo,imagen):
            self.nombre = nombre
            self.costo = costo
            self.imagen=imagen
        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.nombre},'
                f'Costo:{self.costo},'
                f'imagen:{self.imagen}')


class Licores(app.db.Model):  # Creamo la clase modelo para la macros de datos funcion model
        id = app.db.Column(app.db.Integer, primary_key=True)  # para crear las columnas en la macros de datos
        producto_id = app.db.Column(app.db.Integer, app.db.ForeignKey('producto.id'))
        nombre = app.db.Column(app.db.String(255))
        costo=app.db.Column(app.db.Float)
        imagen=app.db.Column(app.db.String(255))

        def __init__(self, nombre,costo,imagen):
            self.nombre = nombre
            self.costo = costo
            self.imagen=imagen
        def __str__(self):
            return (
                f'Id:{self.id},'
                f'Nombre:{self.nombre},'
                f'Costo:{self.costo,}')



#class Comentarios(app.db.Model):
    #caja_comentarios = app.db.Column(app.db.String(255))
    #hora_registro = app.db.Column(app.db.DateTime, default=datetime.datetime.now)
