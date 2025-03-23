from flask_sqlalchemy import SQLAlchemy
from .models import db, User
from werkzeug.security import generate_password_hash



def verificar_usuario(username, email, pas):
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        password = generate_password_hash(pas)
        new_user = User(username=username, email=email ,password=password)
        db.session.add(new_user)
        db.session.commit()
        return True
        
def verificar_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        error = 'El Usuario Ya existe el correo debe ser Unico'
        return error
    else:
        pass