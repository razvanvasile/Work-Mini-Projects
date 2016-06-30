# Setup
import pkg_resources
pkg_resources.require('cothread')
# Stuff you need to import
from cothread.catools import caget, caput, ca_nothing
from cothread.cadef import CAException

# Code
PV = 'LI-RF-MOSC-01:FREQ_SET'

val = caget(PV)
print('Value of {} is {}'.format(PV, val))

# Fails because (I hope) you're the wrong side of the gateway
try:
    caput(PV, val*1.01)
except CAException as e:
    print('Failed to caput: {}'.format(e))
