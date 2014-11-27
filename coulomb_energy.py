# This file contains the various functions I will use through my attempt to calculate the coloumbic energy of a crystal using the ewald summation method.

def pair_energy(charge1, charge2, pos1, pos2):
    energy = 0
    import math

    sep = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2)
    if sep != 0:  # avoid divide by zero for an atom being paired with itself
        energy = ( charge1 * charge2 ) / sep
    return energy


def separation(pos1, pos2):
    import math

    sep = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2)
    return sep


def madelung(limit):
    # Limit is how far out I want to calculate this energy


    refA = [0, 0, 0]  # The fixed A atom we're going to use in a pair energy withg a working atom
    refB = [0.5, 0.5, 0.5]  # Similarly for B
    chargeA = 1  # Charge in terms of electronic charge
    chargeB = -1  # Again
    posA = [0, 0, 0]  # The first value for the working A atom
    posB = [0.5, 0.5, 0.5]  # Similarly for B
    energy = 0  # Initial value for energy

    for z in range(limit):  # stepping out in z, starting with zero deliberately to catch the atoms in the unit cell
        posA[2] += z
        posB[2] += z
        for y in range(limit):  # Stepping outward in y
            posA[1] += y
            posB[1] += y
            for x in range(limit): # STepping outward in x
                posA[0] += x
                posB[0] += x
                # All of the available pairs between reference atoms and working atoms.
                # Need to consider double counting formally
                energy += pair_energy(chargeA, chargeA, refA, posA)

                energy += pair_energy(chargeB, chargeA, refA, posB)

                energy += pair_energy(chargeB, chargeB, refB, posB)

                energy += pair_energy(chargeA, chargeB, refB, posA)


    return energy