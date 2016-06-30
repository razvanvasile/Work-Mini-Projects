# Setup
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap
# Used to extract values off pvs
from cothread.catools import caget

# Load the machine
ap.machines.load('SRI21')

# First task
BPMS = ap.getElements('BPM')
print('There are {} BPM elements in the machine.'.format(len(BPMS)))

# Second task
print('A list of all the PV names for all BPMS')
for BPM in range(len(BPMS)):
    pvs = sorted(BPMS[BPM].pv())
    print('PV names: {}  PV values: {}'.format(pvs, caget(pvs)))

# Third task
QUADS = ap.getElements('QUAD')

print('String values for the setpoint currents:')
for key in range(len(QUADS)):
    print(caget(QUADS[key].pv(handle='readback')))
