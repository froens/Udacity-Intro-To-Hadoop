#!/usr/bin/python

import sys
from datetime import datetime, date, time

topTen = []
oldKey = None
thisKey = None
qCount = 0
aCount = 0

def updateTopTen(d, key, value):
    d.append((key, value))
    d = sorted(d, key=lambda x: x[1])
    if len(d) > 10:
        d = d[1:]
    return d


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, node_type = data_mapped

    if oldKey and oldKey != thisKey:
        topTen = updateTopTen(topTen, oldKey, aCount)
        qCount = 0
        aCount = 0


    oldKey = thisKey

    if node_type == "question":
        qCount += 1
    
    aCount += 1
    

if thisKey:
    topTen = updateTopTen(topTen, oldKey, qCount)

for tt in reversed(topTen):
    k, v = tt
    print "{0}\t{1}".format(k, v)
