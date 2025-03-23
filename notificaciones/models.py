from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#iniciar sesion

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)



class Publicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.String(120), nullable=False)
    hora_inicio = db.Column(db.String(120), nullable=False)
    hora_fin = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)
    organizador = db.Column(db.String(80), nullable=False)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    fecha = db.Column(db.String(120), nullable=False)
    hora_inicio = db.Column(db.String(120), nullable=False)
    hora_fin = db.Column(db.String(120), nullable=False)
    ubicacion = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)
    organizador = db.Column(db.String(80), nullable=False)
