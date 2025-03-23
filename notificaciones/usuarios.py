from flask import Blueprint, render_template, request, url_for, redirect, session
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from .funciones import verificar_user

bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    users = User.query.all()
    return render_template('usuarios/index.html', users=users)

@bp.route('/agregar_usuario')
def v_agregar_usuario():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('usuarios/agregar.html')


@bp.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        existe = verificar_user(email)
        if len(password ) < 8:
            return render_template('usuarios/agregar.html', error='La contraseña debe tener al menos 8 caracteres')
        if '.' not in password:
            return render_template('usuarios/agregar.html', error='La contraseña debe tener al menos un caracter especial (.)')
        if existe:
            return render_template('usuarios/agregar.html', error=existe)
        pas = generate_password_hash(password)
        user = User(username=username, email=email, password=pas)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('usuarios.index'))
    
    


@bp.route('/editar_usuario/<int:id>')
def v_editar_usuario(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(id)
    return render_template('usuarios/editar.html', user=user)


@bp.route('/editar_usuario/<int:id>', methods=['GET','POST'])
def editar_usuario(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        pas = request.form['password'].strip()
        password = generate_password_hash(pas)
        user = User.query.get(id)
        user.username = username
        user.email = email
        user.password = password
        db.session.commit()
        return render_template('usuarios/index.html', users=User.query.all())

@bp.route('/eliminar_usuario/<int:id>')
def eliminar_usuario(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('usuarios.index'))

