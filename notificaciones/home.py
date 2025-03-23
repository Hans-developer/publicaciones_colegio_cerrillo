from flask import Blueprint, render_template, url_for, redirect
from .models import db, Publicacion
from .funciones import verificar_usuario


bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    username = 'admin'
    email = 'admin@gmail.com'
    pas = 'H1q2w3e4r.'
    verificar_usuario(username, email, pas)
    public = Publicacion.query.all()
    return render_template('home/index.html', public=public)