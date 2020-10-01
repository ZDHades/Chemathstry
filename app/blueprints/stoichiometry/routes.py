from .import bp as stoichiometry
from chempy import balance_stoichiometry, Substance, mass_fractions
from .forms import two_part_reaction
from flask_login import current_user, login_required
from .models import StoichQueries
from flask import flash, redirect, render_template, url_for
# changed name of table 
# route to balance an equation
@stoichiometry.route('/', methods=['GET', 'POST'])
@login_required
def do_stoichiometry():
    # set up an instance of the form
    form = two_part_reaction()

    reac = None
    prod = None
    solution = None

    if form.validate_on_submit():
        # collect the data from the form into a dictionary
        data = {
            'reactants' : request.form.get('reactants').split(','),
            'products' : request.form.get('products').split(',')
        }

        # plug in the info to the balance_stoichiometry method
        reac, prod = balance_stoichiometry(data['reactants'], data['products'])

        # create a variable to save the solution
        solution = (f'{dict(reac)}: {dict(prod)}')

        # create an instance of the StoichQuery table
        s = StoichQueries(reactants = data['reactants'], products=data['products'], solution=solution, user_id=current_user.id)

        # save the instance to the database
        db.session.add(s)
        db.session.commit()

        flash(f'')
        return redirect(url_for('stoichiometry.do_stoichiometry'))

    # send the data to the HTML page
    content = {
        'reactants' : reac,
        'products' : prod,
        'solution' : solution,
        'queries' : StoichQueries.query.filter_by(user_id=current_user.id).all()
    }
    return render_template('stoichiometry.html', **content)
