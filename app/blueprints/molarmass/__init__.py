from flask import Blueprint

bp = Blueprint('molarmass', __name__, url_prefix='/molarmass')

from .import models, routes
