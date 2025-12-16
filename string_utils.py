


def split_before_uppercases(formula):
        atoms = {}
    i = 0

    while i < len(formula):
        atom = formula[i]
        i += 1

        num = ""
        while i < len(formula) and formula[i].isdigit():
            num += formula[i]
            i += 1

        atoms[atom] = atoms.get(atom, 0) + (int(num) if num else 1)

    return atomspass  # replace the pass with your code

def split_at_digit(formula):
        atom = ""
    number = ""

    for ch in formula:
        if ch.isdigit():
            number += ch
        else:
            atom += ch

    return atom, int(number) if number else 1pass  # replace the pass with your code

def count_atoms_in_molecule(molecular_formula):
       atoms = {}
    part = ""

    for ch in molecular_formula:
        if ch.isupper() and part:
            atom, count = split_at_digit(part)
            atoms[atom] = atoms.get(atom, 0) + count
            part = ch
        else:
            part += ch 
    atom, count = split_at_digit(part)
    atoms[atom] = atoms.get(atom, 0) + count

    

    return atoms """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

   dict = {} # Step 1: Initialize an empty dictionary to store atom counts

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
       dict += atom_name, atom_count  # Step 2: Update the dictionary with the atom name and count

    return dict# Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
