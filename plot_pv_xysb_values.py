import pkg_resources
pkg_resources.require('aphla')
pkg_resources.require('matplotlib')
import aphla as ap
import matplotlib.pyplot as p
import time
from cothread.catools import caget, caput


# Load the machine
ap.machines.load('SRI21')

# Get all BPMS elements
BPMS = ap.getElements('BPM')

def pv_xysb_values(BPMS):
    ''' Method to return lists of values for x, y and sb properties of a BPM '''
    x_bpm_values = list()
    y_bpm_values = list()
    sb_bpm_values = list()

    for BPM in BPMS:
        # Check if the PV is enabled
        pvs = BPM.pv()
        if ':SA:Y' in pvs[0]:
            pv_enabled = BPM.pv()[0].replace(':SA:Y', ':CF:ENABLED_S')
        else:
            pv_enabled = BPM.pv()[0].replace(':SA:X', ':CF:ENABLED_S')

        # Check if the pv is enabled
        if(caget(pv_enabled)):
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
        if ':SA:Y' in pvs[0]:
            pv_enabled = BPM.pv()[0].replace(':SA:Y', ':CF:ENABLED_S')
        else:
            pv_enabled = BPM.pv()[0].replace(':SA:X', ':CF:ENABLED_S')

        # Check if the pv is enabled
        if(caget(pv_enabled)):
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

print 'Timeit for pvXYSbValues'
start = time.time()
x_bpm_values, y_bpm_values, sb_bpm_values = pv_xysb_values(BPMS)
end = time.time()
print (end - start)

print 'Timeit for pvXYSbValues with caget'
start = time.time()
x_bpm_values, y_bpm_values, sb_bpm_values = pv_xysb_values_with_caget(BPMS)
end = time.time()
print (end - start)

p.ylabel('X/Y BPM Values')
p.xlabel('SB BPM Values')
p.plot(sb_bpm_values, x_bpm_values, 'r', sb_bpm_values, y_bpm_values, 'g')
p.show()
