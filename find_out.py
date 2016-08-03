#!/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/dls-python
''' Display all modules in the APHLA file path '''
import os
import argparse
from subprocess import Popen, PIPE

def create_parser():
    ''' Parse command line arguments: path and search object '''
    parser = argparse.ArgumentParser(description='Location/type of search')
    parser.add_argument("-o", "--object", dest="search_obj",
                        help="argument type: module, package",
                        metavar="OBJECT", default='module')

    required_argv = parser.add_argument_group('required arguments')
    required_argv.add_argument("-p", "--path", dest="path",
                               help="PATH of file to search",
                               metavar="PATH", required=True)

    return parser.parse_args()


def parse_user_settings(argv):
    ''' Used created parser to parse user setings '''
    search_path = argv.path
    search_obj = argv.search_obj
    if search_obj != 'package' and search_obj != 'module':
        print 'Search object must be \'package\' or \'module\''
        exit(-1)

    return search_path, search_obj


def find_data_on_disk(search_path, search_obj):
    ''' Function to find data on disk '''
    if search_obj == 'module':
        p_1 = Popen(['find', search_path, '-name', '*.py'], stdout=PIPE)
    elif search_obj == 'package':
        p_1 = Popen(['find', search_path, '-name', '__init__.py'], stdout=PIPE)
    raw_data = p_1.communicate()[0]
    p_1.stdout.close()

    return raw_data


def parse_data(raw_data, search_path):
    ''' Parse raw data in a more useful format '''
    raw_data = raw_data.strip().split('\n')
    # Remove search_path from the front of each line
    raw_data = [line[len(search_path):] if line.startswith(search_path) else line for line in raw_data]
    # Remove leading slash if present
    raw_data = [line.lstrip('/') for line in raw_data]
    # Split into path and filename.
    raw_data = [os.path.split(line) for line in raw_data]

    return raw_data


def print_results(data, search_obj):
    ''' Print (parsed) data to the screen.
        Data is the in the format [(path, module), (path, module),...].
    '''
    # Sort
    data = sorted(data, key=lambda x: x[0])
    paths = []
    classes = []
    for path, module in data:
        paths.append(path)
        classes.append(module)

    # Print dots between package names (like in python code)
    path_names = [path.replace('/', '.') for path in paths]

    print "{:30s}       {:10s}".format('PACKAGE', 'MODULE')
    for i in range(len(classes)):
        print "{:30s}   |   {:10s}".format(path_names[i], classes[i])

    print 'Total of {0} \'{1}\' objects found.'.format(len(data), search_obj)


def main():
    ''' Docstring '''
    argv = create_parser()
    search_path, search_obj = parse_user_settings(argv)

    raw_data = find_data_on_disk(search_path, search_obj)
    parsed_data = parse_data(raw_data, search_path)
    print_results(parsed_data, search_obj)


if __name__ == "__main__":
    main()
