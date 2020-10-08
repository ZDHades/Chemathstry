from flask import Blueprint

bp = Blueprint('massfraction', __name__, url_prefix='/massfraction')

from .import models, routes
from flask import Blueprint

bp = Blueprint('massfractions', __name__, url_prefix='/massfractions')

from .import models, routes
