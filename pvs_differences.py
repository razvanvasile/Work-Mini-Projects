import pkg_resources
pkg_resources.require('aphla')
import aphla as ap

# Load the machine
ap.machines.load('SRI21')
sri21_pvs = set()

# Find unique pv names for SRI21
elements = ap.getElements('*')

for element in elements:
    pvs = element.pv()
    if (len(pvs) > 0):
        pv_name = pvs[0].split(':')[0]
        sri21_pvs.add(pv_name)
    
# Load the machine
ap.machines.load('VMX')
vmx_pvs = set()

# Find unique pv names for SRI21
elements = ap.getElements('*')

for element in elements:
    pvs = element.pv()
    if (len(pvs) > 0):
        pv_name = pvs[0].split(':')[0]
        vmx_pvs.add(pv_name)

print 'All PVs in \'SRI21\' that are not in \'VMX\''
print sri21_pvs - vmx_pvs
print 'Total difference: ', len(sri21_pvs - vmx_pvs)

print 'All PVs in \'VMX\' that are not in \'SRI21\''
print vmx_pvs - sri21_pvs
print 'Total difference: ', len(vmx_pvs - sri21_pvs)
