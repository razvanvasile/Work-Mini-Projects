import pytac.load_csv
import pytac.epics

def main():
    # First task: print the number of bpm y elements in the ring.
    lattice = pytac.load_csv.load('VMX', pytac.epics.EpicsControlSystem())
    bpms = lattice.get_elements('BPM')
    bpms_n = 0
    try:
        for bpm in bpms:
            bpm.get_pv_name('y')
            bpms_n += 1
        print 'There exist {0} BPMy elements in the ring.'.format(bpms_n)
    except:
        print 'Warning! There exists a bpm with no y field.'

    # Second task: Print each bpmx pv along with the associated value.
    for bpm in bpms:
        print bpm.get_pv_name('x', 'readback')
        print bpm.get_pv_value('x', 'readback')

    # Third task: Print the setpoint pv value for all quadrupoles.
    quads = lattice.get_elements('QUAD')
    for quad in quads:
        print 'Readback value:{0}'.format(quad.get_pv_value('b1', 'readback'))
        print 'Setpoint value:{0}'.format(quad.get_pv_value('b1', 'setpoint'))


if __name__=='__main__':
    main()
