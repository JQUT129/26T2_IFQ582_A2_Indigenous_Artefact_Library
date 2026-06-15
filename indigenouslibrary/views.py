from flask import Blueprint, render_template, request, session
from .models import *
from datetime import datetime

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/artefacts/')
def artefacts():
    return render_template('artefacts.html')


@bp.route('/review/')
def review():
    return render_template('review.html')
