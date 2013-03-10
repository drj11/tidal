#!/usr/bin/env python

from collections import OrderedDict

"""
Values for omega 0 to 6
"""

# Astronomical values from NOAA Glossary [NOAA2000]:
# (These agree with the per century figures from [PUGH1976] Table
# 4:2 for s and h and N for all decimal places, for p for 7 d.p.
# (note that p changes across a century by enough to make a
# difference in the 8th d.p.))
#      T           s           h           p           N
dph = [15.0, None, 0.54901653, 0.04106864, 0.00464183, 0.00220641,
#      p'
       0.00000196]
dph[1] = dph[0]+dph[3]-dph[2]

def read_constituents():
    d = OrderedDict()
    with open('constituents') as f:
        for row in f:
            if row[0] == '#':
                continue
            l = row.split()
            combination = map(int, l[:6])
            name = l[6]
            d[name] = combination
    return d

def main():
    linconst = read_constituents()
    for name,combination in linconst.items():
        speed = sum((k*s) for k,s in zip(combination,dph[1:]))
        print name, speed

if __name__ == '__main__':
    main()
