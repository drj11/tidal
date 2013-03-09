#!/usr/bin/env python

from collections import OrderedDict

"""
Values for omega 0 to 6
"""

# Basic frequencies of astronomical motions, as per [PUGH1976]
# (table 3:2). Note: the 'f' column seems to be the most
# precise; it's in cycles per day.
#      Cs   Cl         s          h          p           N
cpd = [1.0, 0.9661369, 0.0366009, 0.0027379, 0.00030937, 0.0001471,
# p'
  1.0/(365.35*20942)]
# wikipedia
cpd[2] = 1.0/27.32166155  # sidereal lunar month
cpd[3] = 1.0/365.242189   # tropical year
cpd[5] = 1.0/(365.25*18.5996) # wrong definition of year?
# Using the relationship w0+w3=w1+w2
cpd[1] = cpd[0]+cpd[3]-cpd[2]
# angular speeds of above in degrees per hour.
dph = [15.0*f for f in cpd]

# Instead of the above, use the values from NOAA Glossary [NOAA2000]:
#      T           s           h           p           N
dph = [15.0, None, 0.54901653, 0.04106864, 0.00464183, 0.00220641,
#      p'
       0.00000196]
dph[1] = dph[0]+dph[3]-dph[2]
del cpd

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
