import pytac.load_csv
import pytac.epics

def main():
    lattice = pytac.load_csv.load('VMX', pytac.epics.EpicsControlSystem())
    print lattice.get_length()


if __name__=='__main__':
    main()
