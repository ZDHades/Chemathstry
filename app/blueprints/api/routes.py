from .import bp as api
from flask import jsonify
from app.blueprints.authentication.models import User
from app.blueprints.stoichiometry.models import StoichQueries
from app import db

#####################
# Stoich API Routes #
#####################

@api.route('/stoich', methods=['GET'])
def get_stoich_queries():
    """
    [GET] api/stoich
    """
    s = StoichQueries.query.filter_by(user_id=current_user.id).all()
    return jsonify([_.to_dict() for _ in s])

