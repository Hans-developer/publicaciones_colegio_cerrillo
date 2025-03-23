from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('ayuda', __name__, url_prefix='/ayuda')


@bp.route('/ayuda')
def index():
    return render_template('ayuda/index.html')