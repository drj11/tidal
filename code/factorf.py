#!/usr/bin/env python

"""Table of Node factor f, for M2.

Unless otherwise specified:
T measured in Julian centuries with 0 at midnight at Greenwich
meridian for 0/1 January 1900.

Longitudes measured in ecliptic plan from point of Ares. In
degrees.

Compare with
http://www.pac.dfo-mpo.gc.ca/science/oceans/tidal-marees/facteur-node-factor-eng.htm

"""

import math
import sys

def Nat(T):
    """Longitude of lunar ascending node at time T."""
    # [PUGH1976] Table 4:2
    return 259.16 - 1934.14*T + 0.0021*T**2

def factorK1at(T):
    """Node factor f for K1 at Time T."""
    N = math.radians(Nat(T))
    # IHO Constituent List
    f = 1.0060 + 0.1150*math.cos(N) - 0.0088*math.cos(2*N) + 0.0006*math.cos(3*N)
    return f

def factorK2at(T):
    """Node factor f for K2 at Time T."""
    N = math.radians(Nat(T))
    # IHO Constituent List
    f = 1.0246 + 0.2863*math.cos(N) + 0.0083*math.cos(2*N) - 0.0015*math.cos(3*N)
    return f

def factorM2at(T):
    """Node factor f for M2 at time T."""
    N = math.radians(Nat(T))
    # IHO Constituent List
    f = 1.0007 - 0.0373*math.cos(N) + 0.0002*math.cos(2*N)
    return f

def factorO1at(T):
    """Node factor f for O1 at time T."""
    # Note: The IHO apparently publishes the wrong correction.
    # The one used here produces factors that agree with
    # [SCHUREMAN1971] and http://www.pac.dfo-mpo.gc.ca/science/oceans/tidal-marees/facteur-node-factor-eng.htm
    N = math.radians(Nat(T))
    # IHO Constituent List
    # f = 1.0176 + 0.1871*math.cos(N) - 0.0147*math.cos(2*N)
    # Using corrected 1.009 value from [PUGH1976] Table 4:3
    f = 1.009 + 0.1871*math.cos(N) - 0.0147*math.cos(2*N)
    return f

factor = dict(K1=factorK1at, K2=factorK2at, M2=factorM2at, O1=factorO1at)

def TofY(Y):
    """Time T for July 1 in year Y (CE)."""
    # Days between Jan 1 and July 1
    D = 181
    leap = (Y%4 == 0) - (Y%100 == 0) + (Y%400 == 0)
    D += leap
    T = 365*(Y-1900) + D + (Y-1901)//4
    T /= 36525.0
    return T


# There are several factors where IHO and 
# http://www.pac.dfo-mpo.gc.ca/science/oceans/tidal-marees/facteur-node-factor-eng.htm
# differ:
# N2: IHO say to use M2
# P1: IHO say to use a constant 1
# Q1: IHO say to use O1
# S2: Not listed at IHO (drj: why would this have a nodal
# correction?)

def main():
    constituents = "O1 K1 M2 K2".split()
    for year in range(1900,2051):
        T = TofY(year)
        sys.stdout.write("%d" % year)
        for con in constituents:
            f = factor[con](T)
            sys.stdout.write(" %s %6.3f" % (con, f))
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()
