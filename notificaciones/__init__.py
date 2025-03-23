from flask import Flask
from . models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notificaciones.db'
    app.config['SECRET_KEY'] = 'your secret key'
    db.init_app(app)


    from . import home
    from . import auth
    from . import publicacion
    from . import pub_anteriores
    from . import usuarios
    from . import ayuda
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(publicacion.bp)
    app.register_blueprint(pub_anteriores.bp)
    app.register_blueprint(usuarios.bp)
    app.register_blueprint(ayuda.bp)


    with app.app_context():
        db.create_all()

    return app