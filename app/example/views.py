from flask import Blueprint, render_template

from auth.decorators import authentication_required
from auth.user import get_user

bp = Blueprint('example', __name__, url_prefix='/', template_folder='../templates', static_folder='../static')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/dashboard')
@authentication_required
def dashboard():
    user = get_user()
    return render_template('dashboard.html', user=user)
