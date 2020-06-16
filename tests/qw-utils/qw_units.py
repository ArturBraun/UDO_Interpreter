#import numericalunits as un
#un.reset_units('SI')

class units:
    def __init__(self):
        self.GHz = 10 ^ 9

un = units


def setGHzBaseFreqUnit():
    un.GHz = 1
    un.Hz = 10 ^ -9
    un.kHz = 10 ^ -6
    un.MHz = 10 ^ -3
    un.THz = 10 ^ 3
    un.PHz = 10 ^ 6
    un.mHz = 10 ^ -12

def setmmBaseGeomUnit():
    un.mm = 1
    un.m = 10 ^ 3
    un.inch = 25.4
    un.km = 10 ^ 6
    un.um = 10 ^ -3
    un.nm = 10 ^ -6
    un.pm = 10 ^ -9
    #un.mile = un.mile * un.m
