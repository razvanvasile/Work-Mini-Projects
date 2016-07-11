# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap
# Other stuff
from cothread.catools import caget, caput, ca_nothing

# Load the machine
ap.machines.load('SRI21')

# First task
BPMS = ap.getElements('BPM')
print('There are {} BPM elements in the machine.'.format(len(BPMS)))

# Second task
print('A list of all the PV names for all BPMS')
for BPM in range(len(BPMS)):
    print (BPMS[BPM].pv(field='x'))
    print caget(BPMS[BPM].pv())

# Third task
QUADS = ap.getElements('QUAD')

print('String values for the setpoint currents')
for QUAD in range(len(QUADS)):
    print ('Readback value = {}'.format
           (caget(QUADS[QUAD].pv(handle='readback'))))
    print ('Setpoint value = {}'.format
           (caget(QUADS[QUAD].pv(handle='setpoint'))))
