import pytac.load_csv
import pytac.epics


def main():
    lattice = pytac.load_csv.load('VMX', pytac.epics.EpicsControlSystem())
    bpms = lattice.get_elements('BPM')

    disabled_devices = 0
    for bpm in bpms:
        if not bpm._devices['x'].is_enabled():
            disabled_devices += 1
        if not bpm._devices['y'].is_enabled():
            disabled_devices += 1

    print 'There are {0} disabled bpm devices.'.format(disabled_devices)


if __name__=='__main__':
    main()
