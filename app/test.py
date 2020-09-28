from chempy import balance_stoichiometry
from pprint import pprint
reac, prod = balance_stoichiometry(['NH4ClO4', 'Al'], ['Al2O3', 'HCl', 'H2O', 'N2'])

solution = (f'{dict(reac)}: {dict(prod)}')
print(solution)

reactants = 'NH4ClO4, Al'
products = 'Al2O3, HCl, H2O, N2'

