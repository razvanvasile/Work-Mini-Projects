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


if __name__=='__main__':
    main()
