from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/Panel_administracion')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.all()
    return render_template('dashboard/index.html', user=user)


@bp.route('/iniciar_sesion')
def v_login():
    return render_template('auth/login.html')


@bp.route('/iniciar_sesion', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard.index'))
        else:
            return render_template('auth/login.html', error='Credenciales incorrectas')
    
    return render_template('auth/login.html')
    

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home.index'))
    
