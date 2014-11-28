__author__ = 'Rob'


def atom_pair_energy(atom1, atom2):
    energy = 0
    import math
    sep = math.sqrt((atom1[0] - atom2[0]) ** 2 + (atom1[1] - atom2[1]) ** 2 + (atom1[2] - atom2[2]) ** 2)
    if sep != 0:  # avoid divide by zero for an atom being paired with itself
        energy = (atom1[3] * atom2[3]) / sep
    return energy


def unit_cell_pair_energy(atom_list1, atom_list2):
    energy = 0
    for atom1 in atom_list1:
        for atom2 in atom_list2:
            energy += atom_pair_energy(atom1, atom2)
    return energy


def separation(atom1, atom2):
    import math
    sep = math.sqrt((atom1[0] - atom2[0]) ** 2 + (atom1[1] - atom2[1]) ** 2 + (atom1[2] - atom2[2]) ** 2)
    return sep


def madelung_sum(atoms_in_unit_cell, limit):
    current_atoms = []
    for atom in atoms_in_unit_cell:
        current_atoms.append(atom[:])
    energy = 0  # Initial value for energy
    for z in range(-limit, limit):  # stepping across z
        for atom in current_atoms:
            atom[2] += z
        for y in range(-limit, limit):  # Stepping across y
            for atom in current_atoms:
                atom[1] += y
            for x in range(-limit, limit):  # Stepping across x
                for atom in current_atoms:
                    atom[0] += x
                energy += unit_cell_pair_energy(current_atoms, atoms_in_unit_cell)
    return energy