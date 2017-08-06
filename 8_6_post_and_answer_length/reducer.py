#!/usr/bin/python

import sys
from datetime import datetime, date, time

oldKey = None
thisKey = None
currentSum = 0
currentCount = 0
qLen = -1

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, node_type, body_len = data_mapped

    if oldKey and oldKey != thisKey:
        if currentCount > 0:
            mean = currentSum / currentCount
            print "{0}\t{1}\t{2}".format(oldKey, qLen, mean)
        else:
            print "{0}\t{1}\t{2}".format(oldKey, qLen, 0)
        qLen = -1
        currentSum = 0
        currentCount = 0

    oldKey = thisKey

    if node_type == "answer":
        currentSum += float(body_len)
        currentCount += 1
    elif node_type == "question":
        qLen = float(body_len)
    

if thisKey:
    if currentCount > 0:
        mean = currentSum / currentCount
        print "{0}\t{1}\t{2}".format(oldKey, qLen, mean)
    else:
        print "{0}\t{1}\t{2}".format(oldKey, qLen, 0)
