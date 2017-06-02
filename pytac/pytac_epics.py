import pytac.epics

def main():
    pv='LI-RF-MOSC-01:FREQ_SET'
    epics = pytac.epics.EpicsControlSystem()

    try:
        epics.put(pv, 4)
    except:
        print "Ooops! You don't have right access to set the pv."


if __name__=='__main__':
    main()
