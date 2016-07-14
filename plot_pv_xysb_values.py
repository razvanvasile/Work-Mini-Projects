# This program contains methods to:
#   - extract x, y and sb values for pvs inside all BPM
#     elements using caget and BPM.get().
#   - plot the x, y BPM coordinates against sb using matplotlib and scisoftpy.
import time
import pkg_resources
try:
    pkg_resources.require('aphla')
    import numpy
    from cothread.catools import caget
    import aphla as ap
    # Setup
    ap.machines.load('SRI21')
except (pkg_resources.DistributionNotFound, ImportError) as err:
    print str(err)
    print ''' Error importing one of the libraries: pkg_resources, aphla. '''
    import sys
    sys.exit()


def bpm_enabled(bpm):
    ''' Check if BPM is enabled using caget. '''
    pvs = bpm.pv()
    # Assume that all PVs have the same prefix
    pv_enabled = '{0}:CF:ENABLED_S'.format(pvs[0].split(':')[0])
    return caget(pv_enabled)


def pv_xysb_values(BPMS):
    ''' Method to return lists of values for x, y and sb properties of a BPM '''
    x_bpm_values = list()
    y_bpm_values = list()
    sb_bpm_values = list()

    for BPM in BPMS:
        # Check if the pv is enabled
        if(bpm_enabled(BPM)):
            # Get its value and store it in the list
            x_bpm_values.append(BPM.get('x', handle='readback'))
            y_bpm_values.append(BPM.get('y', handle='readback'))
            sb_bpm_values.append(BPM.sb)
        else:
            print 'Found a BPM which is not enabled'

    return x_bpm_values, y_bpm_values, sb_bpm_values


def pv_xysb_values_with_caget(BPMS):
    ''' Method to return lists of values for x, y and sb properties of a BPM
        using caget '''
    x_bpm_values = list()
    y_bpm_values = list()
    sb_bpm_values = list()

    for BPM in BPMS:
        pvs = BPM.pv()
        # Check if the pv is enabled
        if(bpm_enabled(BPM)):
            # Get its value and store it in the list
            if ':Y' in pvs[0]:
                y_bpm_values.append(pvs[0])
                x_bpm_values.append(pvs[1])
                sb_bpm_values.append(BPM.sb)
            else:
                x_bpm_values.append(pvs[0])
                y_bpm_values.append(pvs[1])
                sb_bpm_values.append(BPM.sb)
        else:
            print "Found a pv value which is not enabled"

    x_bpm_values = caget(x_bpm_values)
    y_bpm_values = caget(y_bpm_values)

    return x_bpm_values, y_bpm_values, sb_bpm_values


def plot_with_scisoftpy():
    a = dnp.arange(1,10.)
    b = dnp.arange(3,14.)
    dnp.plot.line([a,a+12.3]) # plots two lines against array index
    dnp.plot.line(2*a, [a,a+12.3]) # plots two lines against 2*a
    dnp.plot.line([2*a, 3.5*b], [a,b]) # plots two lines against defined x values


def time_function(my_function, my_args):
    ''' Method to time '''
    print 'Timing {0}'.format(my_function.__name__)
    start = time.time()
    x_bpm_values, y_bpm_values, sb_bpm_values = my_function(my_args)
    end = time.time()
    print (end - start)

    return x_bpm_values, y_bpm_values, sb_bpm_values


BPMS = ap.getElements('BPM')
x_bpm_values, y_bpm_values, sb_bpm_values = time_function(pv_xysb_values, BPMS)
x_bpm_values, y_bpm_values, sb_bpm_values = time_function(pv_xysb_values_with_caget, BPMS)

try:
    print """ Trying to plot the values using Scisoftpy. """
    import scisoftpy.plot as dpl

    dpl.plot(numpy.array(sb_bpm_values), [numpy.array(x_bpm_values), numpy.array(y_bpm_values)])
except ImportError as err:
    print str(err)
    print """ Scisoftpy was probably not found. Will try using matplotlib. """
    pkg_resources.require('matplotlib')
    import matplotlib.pyplot as p

    p.ylabel('X/Y BPM Values')
    p.xlabel('SB BPM Values')
    p.plot(sb_bpm_values, x_bpm_values, 'r', sb_bpm_values, y_bpm_values, 'g')
    p.show()
