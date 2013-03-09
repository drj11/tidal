#!/usr/bin/env python

"""
Reads in frequencies from frequencies file, and outputs an R
formula to use in a linear model.
"""

import math
import sys

def main():
    inp = open('frequencies')
    out = sys.stdout
    fs = []
    for row in inp:
        if row[0] == '#':
            continue
        f = float(row.split()[1])
        # Convert from degrees per hour to radian per hour:
        f *= math.pi/180.0
        fs.append(f)
    out.write('+'.join("sin(%r*t)+cos(%r*t)" % (f,f) for f in fs))
    out.write('\n')

if __name__ == '__main__':
    main()

