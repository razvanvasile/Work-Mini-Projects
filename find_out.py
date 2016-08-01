#!/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/dls-python
''' Display all modules in the APHLA file path '''
import argparse
from subprocess import Popen, PIPE

def create_parser():
    ''' Parse command line arguments: path and search object '''
    parser = argparse.ArgumentParser(description='Location/type of search')
    parser.add_argument("-o", "--object", dest="search_obj",
                        help="argument type: class, function",
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
    raw_data = [line.split(':') for line in raw_data.split('\n')]
    del raw_data[-1]
    if search_path.endswith('/'):
        search_path = search_path[:-1]
    raw_data = [line[0].split(search_path) for line in raw_data]
    raw_data = [line[1].split('/') for line in raw_data]
    for line in raw_data:
        del line[0]

    return raw_data


def print_results(data, search_obj):
    ''' Print (parsed) data to the screen '''
    paths = []
    classes = []
    for line in data:
        paths.append(line[:-1])
        classes.append(line[-1])

    path_names = []
    for line in paths:
        path_names.append(".".join(line))

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
