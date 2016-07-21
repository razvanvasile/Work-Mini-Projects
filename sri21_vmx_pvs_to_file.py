#!/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/dls-python

from utilities import get_pv_names, write_pvs_to_file
import argparse

parser = argparse.ArgumentParser('optional named arguments')
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE", default = 'test.txt')

requiredArgv = parser.add_argument_group('required arguments')
requiredArgv.add_argument("-m", "--mode", dest="mode",
                          help="Machine MODE to use", metavar="MODE", required = True)

argv = parser.parse_args()


mode_pvs = get_pv_names(argv.mode)
write_pvs_to_file(argv.filename, mode_pvs)

print argv.filename
