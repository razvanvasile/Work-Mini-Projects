import pytac.load_csv
import pytac.epics

def main():
    lattice = pytac.load_csv.load('VMX', pytac.epics.EpicsControlSystem())
    families = lattice.get_all_families()
    fin = open('elements_number_in_families.txt', 'w')

    for family in families:
        elements_in_fam = lattice.get_elements(family)
        elements_number = len(elements_in_fam)
        if elements_number == 1:
            fin.write('There is {0} element in the {1} family.\n'
                      .format(elements_number, family))
        else:
            fin.write('There are {0} elements in the {1} family.\n'
                      .format(elements_number, family))

    fin.close()

if __name__=='__main__':
    main()
