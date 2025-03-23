from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import db, Publicacion, Data, User


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    tu = User.query.count()
    tp =  Publicacion.query.count()
    publicaciones = Publicacion.query.all()
    return render_template('dashboard/index.html', publicaciones=publicaciones, tp=tp, tu=tu)


@bp.route('/add_publicacion', methods=['POST'])
def add_publicacion():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        titulo = request.form['titulo'].strip()
        tipo = request.form['tipo'].strip()
        fecha = request.form['fecha'].strip()
        hora_inicio =  request.form['hora_inicio'].strip()
        hora_fin =  request.form['hora_fin'].strip()
        ubicacion =  request.form['ubicacion'].strip()
        descripcion =  request.form['descripcion'].strip()
        organizador = request.form['organizador'].strip()
        new_publicacion = Publicacion(titulo=titulo, tipo=tipo, fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin, ubicacion=ubicacion, descripcion=descripcion, organizador=organizador )
        new_data = Data(titulo=titulo, tipo=tipo, fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin, ubicacion=ubicacion, descripcion=descripcion, organizador=organizador )
        db.session.add(new_publicacion)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return redirect(url_for('dashboard.index'))


@bp.route('/editar_publicacion/<int:id>')
def v_editar_publicacion(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    pub = Publicacion.query.get(id)
    return render_template('dashboard/editar.html', pub=pub)


@bp.route('/editar_publicacion/<int:id>', methods=['GET','POST'])
def editar_publicacion(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    pub = Publicacion.query.get_or_404(id)
    if request.method == 'POST':
        pub.titulo = request.form['titulo'].strip()
        pub.tipo = request.form['tipo'].strip()
        pub.fecha = request.form['fecha'].strip()
        pub.hora_inicio = request.form['hora_inicio'].strip()
        pub.hora_fin = request.form['hora_fin'].strip()
        pub.ubicacion = request.form['ubicacion'].strip()
        pub.descripcion = request.form['descripcion'].strip()
        pub.organizador = request.form['organizador'].strip()
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return redirect(url_for('dashboard.index'))

@bp.route('/eliminar_publicacion/<int:id>')
def eliminar_publicacion(id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    pub = Publicacion.query.get(id)
    db.session.delete(pub)
    db.session.commit()
    return redirect(url_for('dashboard.index'))




    

