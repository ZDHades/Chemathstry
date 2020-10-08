from .import bp as molarmass
from chempy import balance_stoichiometry, Substance, mass_fractions
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from .forms import MolarMass
from .models import MMQueries
from sqlalchemy import desc

# Route for finding the molar mass of a molecule
@molarmass.route('/', methods=['GET','POST'])
@login_required
def get_MM():
    # Set up an instance of the form
    form = MolarMass()

    query = None
    solution = None

    if form.validate_on_submit():
        # collect the data from the form
        query = str(request.form.get('q_MM'))

        # plug it into the formula

        checked = False
        while not checked:
            try:
                checking = Substance.from_formula(query)
                solution = checking.mass
                # create an instance of the MMQueries table
                m = MMQueries(q_MM=query, s_MM=solution, user_id=current_user.id)
                # Save to database
                db.session.add(m)
                db.session.commit()
                checked=True
            # error handeling
            except Exception:
                flash("There was an error in query, solution cannot be determined. Please try again", 'danger')
                return redirect(url_for('molarmass.get_MM'))
        flash("Query Submitted!", 'success')
        return redirect(url_for('molarmass.get_MM'))
    # sending content to the frontend
    content = {
        'Query' : MMQueries.query.filter_by(user_id=current_user.id).order_by(desc('created_on')).first(),
        'form' : form
    }
    return render_template('molarmass.html', **content)

# route to get all queries by user
@molarmass.route('/mmqueries')
@login_required
def mm_queries():
    if current_user.is_authenticated:
        my_queries = current_user.mm_queries
    else:
        my_queries = []
    return render_template('mmqueries.html', queries=my_queries)