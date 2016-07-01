# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap

# Load the machine
ap.machines.load('SRI21')

my_lattice = ap.machines.getLattice()

# Create a dictionary to store a count for each family
family_count = {}

# Part 1
# Initialize the dictionary
for key in range(my_lattice.size()):
    element = my_lattice[key]
    family_count[element.family] = 0

# Find the number of objects existant in each family
for key in range(my_lattice.size()):
    element = my_lattice[key]
    family_count[element.family] += 1

# Print count of each family
for key in range(my_lattice.size()):
    element = my_lattice[key]
    print "Family {}, count {}".format(
        element.family, 
        family_count[element.family])


# Part 2 - all the groups associated with each family
groups_dict = {}

# Initialize the dictionary
for key in range(my_lattice.size()):
    element = my_lattice[key]
    groups_dict[element] = set()

# Do the union between each entry in the dictionary
# and each element
for key in range(my_lattice.size()):
    element = my_lattice[key]
    groups_dict[element] = groups_dict[element].union(element.group)

# Print the set of groups for each entry
for key in range(my_lattice.size()):
    element = my_lattice[key]
    print "Element {}, related groups {}".format(
        element.family, groups_dict[element])
    
