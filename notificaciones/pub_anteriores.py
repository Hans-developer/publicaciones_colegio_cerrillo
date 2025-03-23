from flask import Blueprint, render_template, url_for, redirect, flash
from .models import db, Data

bp = Blueprint('anteriores', __name__, url_prefix='/anteriores')


@bp.route('/')
def index():
    public = Data.query.all()
    return render_template('pasadas/index.html', public=public)