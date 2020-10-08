from flask import current_app as app
from app import create_app, cli, db
from app.blueprints.authentication.models import User
from app.blueprints.stoichiometry.models import StoichQueries
from app.blueprints.molarmass.models import MMQueries

app = create_app()
cli.register(app)

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, "StoichQueries": StoichQueries, 'MMQueries': MMQueries}