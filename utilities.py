# Function to return a list of pvs from a given file

import pkg_resources
pkg_resources.require('aphla')
import aphla as ap


def get_pv_names(mode):
    ''' Given a certain ring mode as a string, return all available pvs  '''
    ap.machines.load(mode)
    result = set()

    elements = ap.getElements('*')
    for element in elements:
        pvs = element.pv()
        if(len(pvs) > 0):
            pv_name = pvs[0].split(':')[0]
            result.add(pv_name)

    return result


def get_pvs_from_file(filepath):
    ''' Return a list of pvs from a given file '''
    with open(filepath) as f:
        contents = f.read().splitlines()
    return contents


def write_pvs_to_file(filename, data):
    ''' Write given pvs to file '''
    f = open(filename, 'w')
    for element in data:
        f.write(element + '\n')
    f.close()
