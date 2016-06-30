# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap

# Load the machine
ap.machines.load('SRI21')

myLattice = ap.machines.getLattice()

length = 0
for key in range(myLattice.size()):
    length += myLattice[key].length

print "The length of the lattice is {}.".format(length)
