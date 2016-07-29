#!/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/dls-python
''' Short script to find all classes and functions inside the APHLA library '''
import argparse
from subprocess import Popen, PIPE

def create_parser():
    ''' Parse command line arguments: path and search object '''
    parser = argparse.ArgumentParser(description='Location/type of search')
    parser.add_argument("-o", "--object", dest="search_obj",
                        help="argument type: class, function",
                        metavar="OBJECT", default='class')
    parser.add_argument("--hide", dest="hide",
                        help='HIDE private functions/classes',
                        action='store_true')

    required_argv = parser.add_argument_group('required arguments')
    required_argv.add_argument("-p", "--path", dest="path",
                               help="PATH of file to search",
                               metavar="PATH", required=True)

    return parser.parse_args()


def parse_user_settings(argv):
    ''' Used created parser to parse user setings '''
    search_path = argv.path
    if 'function' in argv.search_obj:
        search_obj = 'def'
    else:
        search_obj = argv.search_obj
    if argv.hide:
        search_hide = ' _'
    else:
        search_hide = ''

    return search_path, search_obj, search_hide


def find_data_on_disk(search_path, search_obj, search_hide):
    ''' Function to find data on disk '''
    p_1 = Popen(["find", search_path, "-name", "*.py"], stdout=PIPE)
    p_2 = Popen(["xargs", "grep", '-ne', '^' + search_obj + search_hide],
                stdin=p_1.stdout, stdout=PIPE)
    p_1.stdout.close()
    raw_data = p_2.communicate()[0]

    return raw_data


def parse_data(raw_data):
    ''' Parse raw data in a more useful format '''
    raw_data = [line.split(':') for line in raw_data.split('\n')]
    del raw_data[-1]
    for index in range(len(raw_data)):
        if len(raw_data[index]) == 4:
            del raw_data[index][3]

    return raw_data


def print_results(data, search_obj):
    ''' Print (parsed) data to the screen '''
    for line in data:
        print line[0], line[1], '\n', line[2]
    print 'Total of {0} \'{1}\' objects found.'.format(len(data), search_obj)


def main():
    ''' Docstring '''
    argv = create_parser()
    search_path, search_obj, search_hide = parse_user_settings(argv)

    raw_data = find_data_on_disk(search_path, search_obj, search_hide)
    parsed_data = parse_data(raw_data)
    print_results(parsed_data, search_obj)

if __name__ == "__main__":
    main()
