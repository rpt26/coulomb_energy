# This file contains the various functions I will use through my attempt to calculate the coloumbic energy of a crystal.
# This will be done with rather brute force methods initially, possibly moving to the more elegant Ewald sum.

import coulomb_utils


chargeA = 1  # Charge in terms of electronic charge
chargeB = -1  # Again
refA = [0, 0, 0, chargeA]  # The fixed A atom we're going to use in a pair energy withg a working atom
refB = [0.5, 0.5, 0.5, chargeB]  # Similarly for B


reference_atoms = [refA, refB]
energy = 0

file = open('convergence.out', 'a')
for number in range(500):
    energy += coulomb_utils.madelung_sum(reference_atoms, number)
    string = str(number) + ' ' + str(energy)
    file.write(string + '\n')
    print(number, energy)

file.close()