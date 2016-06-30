# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap

# Load the machine
ap.machines.load('SRI21')

my_lattice = ap.machines.getLattice()

length = 0
for key in range(my_lattice.size()):
    length += my_lattice[key].length

print "The length of the lattice is {}.".format(length)
