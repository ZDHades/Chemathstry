from .import bp as massfractions
from chempy import balance_stoichiometry, Substance, mass_fractions
from .forms import mass_fraction
from flask_login import current_user, login_required
from .models import MFQueries
from flask import flash, redirect, render_template, url_for, request
from app import db
from sqlalchemy import desc

# route for getting the mass fractions
@massfractions.route('/', methods=['GET', 'POST'])
@login_required
def get_MF():
    # Set up an instance of the form
    form = mass_fraction()

    reac = None
    prod = None
    solution = []
    
    if form.validate_on_submit():
        # Collect the data from the form into a dictionary
        data ={
            'reactants' : [_strip() for _ in request.form.get('reactants').split(',')],
            'products' : [_strip() for _ in request.form.get('products').split(',')]
        }
        # try except block

        checked = False
        while not checked:
            try:
                # plug in the info to the required methods
                reac, prod  = balance_stoichiometry(data['reactants'], data['products'])
                for fractions in map(mass_fractions, [reac, prod]):
                    solution.append({k: '{0:.3g} wt%'.format(v*100) for k, v in fractions.items()})
                
                s = MFQueries(q_reactants=data['reactants'], q_products=data['products'], solution=solution, user_id=current_user.id )
                db.session.add(s)
                db.session.commit()
                checked = True
            except ValueError:
                flash("There was an error in query, solution cannot be determined. Please try again", 'danger')
                return redirect(url_for('stoichiometry.do_stoichiometry'))
        flash(f'Query Submitted!', 'success')
        return redirect(url_for('massfractions.get_MF'))
    
    # Send the data to the HTML page
    content = {
        'Query': MFQueries.query.filter_by(user_id=current_user.id).order_by(desc('created_on')).first(),
        'form' : form
    }
    return render_template('massfractions.html', **content)

        