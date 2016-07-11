# Load the machine
import pkg_resources
pkg_resources.require('aphla')
import aphla as ap
# Import caget and caput
from cothread.catools import caget, caput

# Load the machine
ap.machines.load('SRI21')
