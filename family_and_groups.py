# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap

# Load the machine
ap.machines.load('SRI21')
my_lattice = ap.machines.getLattice()

# Part 1 - count the number of entries in each family
# Create a dictionary to store a count for each family
family_dict = {}

# Initialize the dictionary
for element in my_lattice.getElementList('*'):
    family_dict[element.family] = 0

# Find the number of objects existant in each family
for element in my_lattice.getElementList('*'):
    family_dict[element.family] += 1

# Print count of each family
for family in family_dict.keys():
    print "Family {}, count {}".format(family,
                                       family_dict[family])


# Part 2 - all the groups associated with each family
my_dict = {}

# Initialize the dictionary
for element in my_lattice.getElementList('*'):
    my_dict[element.family] = set()

# Do the union between each entry in the dictionary
# and each element
for element in my_lattice.getElementList('*'):
    my_dict[element.family] = my_dict[element.family].union(element.group)

# Print the set of groups for each entry
for element in my_dict.keys():
    print "Family {}, related groups {}".format(
        element, my_dict[element])
