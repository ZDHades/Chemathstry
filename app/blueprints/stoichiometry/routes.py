from .import bp as stoichiometry
from chempy import balance_stoichiometry, Substance, mass_fractions
from .forms import two_part_reaction
from flask_login import current_user, login_required
from .models import StoichQueries
from flask import flash, redirect, render_template, url_for, request
from app import db

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
        # Try/except block so if theres an error the page doesnt break
        Checked = False
        while not Checked:
            try:
                reac, prod = balance_stoichiometry(data['reactants'], data['products'])

                # create a variable to save the solution
                solution = (f'{str(reac)[13:-2]} = {str(prod)[13:-2]}')
                s_reac = str(reac)[13:-2]
                s_prod = str(prod)[13:-2]
                # create an instance of the StoichQuery table
                s = StoichQueries(q_reactants = data['reactants'], q_products=data['products'], s_products=s_prod, s_reactants=s_reac, user_id=current_user.id)

                # save the instance to the database
                db.session.add(s)
                db.session.commit()
                Checked = True
            except ValueError:
                flash("There was an error in query, solution cannot be determined. Please try again", 'danger')
                return redirect(url_for('stoichiometry.do_stoichiometry'))

        flash(f'Query Submitted!', 'success')
        return redirect(url_for('stoichiometry.do_stoichiometry'))

    # send the data to the HTML page
    content = {
        'Query' : StoichQueries.query.filter_by(user_id=current_user.id).first(),
        'form' : form
    }
    return render_template('stoichiometry.html', **content)

@stoichiometry.route('/stoichqueries')
@login_required
def stoich_queries():
    if current_user.is_authenticated:
        my_queries = StoichQueries.my_queries().all()
    else:
        my_queries = []
    return render_template('stoichqueries.html', queries=my_queries)

