# Script to compare the pv values of all elements from machine modes
# SRI21 and VMX. Also compares read data to two data sets stored on
# disk.

import pkg_resources
pkg_resources.require('aphla')
import aphla as ap
from utilities import get_pv_names, get_pvs_from_file

sri21_pvs = get_pv_names('SRI21')
vmx_pvs = get_pv_names('VMX')

print 'All PVs in \'SRI21\' that are not in \'VMX\''
print sri21_pvs - vmx_pvs
print 'Total difference: {0}.'.format(len(sri21_pvs - vmx_pvs))

print 'All PVs in \'VMX\' that are not in \'SRI21\''
print vmx_pvs - sri21_pvs
print 'Total difference: {0}.'.format(len(vmx_pvs - sri21_pvs))

# Part 2: Compare computed pv sets with recorded data from files
added_magnets = get_pvs_from_file('data/added_magnets.txt')
removed_magnets = get_pvs_from_file('data/removed_magnets.txt')

print 'Intersection of removed_magnets and sri21_pvs: {0}. Total: {1}.' \
    .format(set(added_magnets) & sri21_pvs, len(set(added_magnets) & sri21_pvs))
print 'Intersection of added_magnets and vmx_pvs: {0}. Total: {1}.' \
    .format(set(removed_magnets) & vmx_pvs, len(set(removed_magnets) & vmx_pvs))
