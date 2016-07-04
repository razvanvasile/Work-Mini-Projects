import pkg_resources
from timeit import timeit
pkg_resources.require('aphla')
pkg_resources.require('matplotlib')
import aphla as ap
import matplotlib.pyplot as p
import timeit
from cothread.catools import caget, caput


# Load the machine
ap.machines.load('SRI21')

# Get all BPMS elements
BPMS = ap.getElements('BPM')

''' Method to return lists of values for x, y and sb properties of a BPM '''
def pvXYSbValues(BPMS):
    xBPMValues = list()
    yBPMValues = list()
    sbBPMValues = list()
    
    for BPM in range(len(BPMS)):
        # Check if the PV is enabled
        pvValue = BPMS[BPM].pv()
        if ':SA:Y' in pvValue[0]:
            pvEnabled = BPMS[BPM].pv()[0].replace(':SA:Y', ':CF:ENABLED_S')
        else:
            pvEnabled = BPMS[BPM].pv()[0].replace(':SA:Y', ':CF:ENABLED_S')
        
        # Check if the pv is enabled
        if(caget(pvEnabled)):
            # Get its value and store it in the list
            xBPMValues.append(BPMS[BPM].get('x', handle='readback'))
            yBPMValues.append(BPMS[BPM].get('y', handle='readback'))
            sbBPMValues.append(BPMS[BPM].sb)
        else:
            print 'Found a BPM which is not enabled'
    
    return xBPMValues, yBPMValues, sbBPMValues

''' Method to return lists of values for x, y and sb properties of a BPM 
    using caget '''
def pvXYSbValuesWithCAGet(BPMS):
    xBPMValues = list()
    yBPMValues = list()
    sbBPMValues = list()
    
    for BPM in range(len(BPMS)):
        # Check if the PV is enabled
        pvValue = BPMS[BPM].pv()
        if ':SA:Y' in pvValue[0]:
            pvEnabled = BPMS[BPM].pv()[0].replace(':SA:Y', ':CF:ENABLED_S')
        else:
            pvEnabled = BPMS[BPM].pv()[0].replace(':SA:X', ':CF:ENABLED_S')

        # Check if the pv is enabled
        if(caget(pvEnabled)):
            # Get its value and store it in the list
            if ':Y' in pvValue[0]:
                yBPMValues.append(caget(pvValue[0]))
                xBPMValues.append(caget(pvValue[1]))
                sbBPMValues.append(BPMS[BPM].sb)
            else:
                xBPMValues.append(caget(pvValue[0]))
                yBPMValues.append(caget(pvValue[1]))
                sbBPMValues.append(BPMS[BPM].sb)
        else:
            print "Found a pv value which is not enabled"

    return xBPMValues, yBPMValues, sbBPMValues


print 'Timeit for pvXYSbValues'
start = timeit.timeit()
xBPMValues, yBPMValues, sbBPMValues = pvXYSbValues(BPMS)
end = timeit.timeit()
print (end - start)

print 'Timeit for pvXYSbValues with caget'
start = timeit.timeit()
xBPMValues, yBPMValues, sbBPMValues = pvXYSbValuesWithCAGet(BPMS)
end = timeit.timeit()
print (end - start)

p.ylabel('X/Y BPM Values')
p.xlabel('SB BPM Values')
p.plot(sbBPMValues, xBPMValues, 'r', sbBPMValues, yBPMValues, 'g')
p.show()
