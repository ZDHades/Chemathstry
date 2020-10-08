from chempy import balance_stoichiometry, Substance
from pprint import pprint
# reac, prod = balance_stoichiometry(['NH4ClO4', 'Al'], ['Al2O3', 'HCl', 'H2O', 'N2'])


#Crud for all routes

# placeholder for reactants = 

    # placeholder for products = 
    

reac, prod = balance_stoichiometry(['NH4ClO4', 'Al'], ['Al2O3', 'HCl', 'H2O', 'N2'])
solution = (f'{str(reac)[13:-2]} = {str(prod)[13:-2]}')

print(solution)
# prod = ['Al2O3', 'HCl', 'H2O', 'N2']
# prods = []
# reac = ['NH4ClO4', 'Al']
# reacs = []

# for chem in prod:
#     Name = Substance.from_formula(chem)
#     prods.append(Name.unicode_name)
#     # print(Name.unicode_name)
# for chem in reac:
#     Name = Substance.from_formula(chem)
#     reacs.append(Name.unicode_name)
#     # print(Name.unicode_name)
# a, b = balance_stoichiometry(reacs, prods)

# # Learn how backref works


# print(f'{str(reac)[13:-2]}')

test = input("test")
yeet = Substance.from_formula(test)
print(yeet.mass)