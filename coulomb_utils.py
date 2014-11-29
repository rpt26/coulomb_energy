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


def madelung_sum(atoms_in_unit_cell, limit, plane, offset):
    # This functions takes a unit cell (assumed to be cubic) of atoms in the form of a list of atoms, where each atom is
    # a list consisting of it's position and charge: [x,y,z,q]. It creates a copy of the list of atoms which I have
    # termed current_atoms. It is this set that are offset with each iteration of the function. Each atom in the current
    # cell are compared back to the original unit cell, atoms_in_unit_cell using the pair energy function defined above.
    # Finally I will be adding a test just before the calculation in energy that will allow us to identify atoms on
    # one side of an arbitrary plane, as a list [h,k,l] following the crystallography conventions, in a cubic crystal
    # this is also a vector perpendicular to the plane in question. We can apply an offset, another vector, to those
    # atoms on one side and not the other. The energy vs offset might be relevant to the plastic properties of the
    # material.

    current_atoms = []  # Here's an empty list to fill with atoms which we can then move around
    for atom in atoms_in_unit_cell:
        current_atoms.append(atom[:])
    energy = 0  # Initial value for energy
    for z in range(-limit, limit):  # Stepping across z
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