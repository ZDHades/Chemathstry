from .import bp as stoichiometry
from chempy import balance_stoichiometry, Substance, mass_fractions
from pprint import pprint
from .forms import two_part_reaction
from flask_login import current_user, login_required
from .models import Stoich_queries

# route to balance an equation
@stoichiometry.route('/', methods=['GET', 'POST'])
@login_required
def do_stoichiometry():
    # Set up an instance of the form
    form = two_part_reaction()

    if form.validate_on_submit():
        # collect the data into a dictionary
        data = {
            'reactants' : request.form.get('reactants').split(','),
            'products' : request.form.get('products').split(',')
        }
        # plug in the info to the balance_stoichiometry method
        reac, prod = balance_stoichiometry(data['reactants'], data['products'])
    # create a variable to save the solution
    solution = (f'{dict(reac)}: {dict(prod)}')
    # create an instance of the Stoich_query table
    s = Stoich_queries(reactants = data['reactants'], products=data['products'], solution=solution, user_id=current_user.id)
    # save the instance to the database
    db.session.add(s)
    db.session.commit()
    # send the data to the HTML page
    content = {
        'reactants' : reac,
        'products' : prod,
        'solution' : solution,
        'queries' : Stoich_queries.query.filter_by(user_id=current_user.id).all()
    }
    return render_template('stoichiometry.html', **content)
