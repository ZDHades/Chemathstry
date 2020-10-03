from chempy import balance_stoichiometry
from pprint import pprint
# reac, prod = balance_stoichiometry(['NH4ClO4', 'Al'], ['Al2O3', 'HCl', 'H2O', 'N2'])


#Crud for all routes

# placeholder for reactants = 

    # placeholder for products = 
    

reac, prod = balance_stoichiometry(['NH4ClO4', 'Al'], ['Al2O3', 'HCl', 'H2O', 'N2'])
solution = (f'{str(reac)[13:-2]} = {str(prod)[13:-2]}')

print(solution)