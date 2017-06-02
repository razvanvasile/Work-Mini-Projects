import pytac.load_csv
import pytac.epics


def write_data_to_file(file_name, data):
    fin = open(file_name, 'w')
    for row in data:
        fin.write('{0}\n'.format(row))
    fin.close()


def get_readback_pvs(mode):
    lattice = pytac.load_csv.load(mode, pytac.epics.EpicsControlSystem())
    elements = lattice.get_elements()
    readback_pvs = list()

    # Get the readback pvs of all elements
    for element in elements:
        fields = element.get_fields()
        for field in fields:
            readback_pvs.append(element.get_pv_name(field, 'readback'))
    return readback_pvs


def main():
    readback_pvs = get_readback_pvs('VMX')

    # Sort the result. It is required for comparison with the Matlab result.
    readback_pvs = sorted(readback_pvs)
    write_data_to_file('readback_pvs_py.txt', readback_pvs)

if __name__=='__main__':
    main()
