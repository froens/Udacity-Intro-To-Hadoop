#!/usr/bin/python

import sys
from datetime import datetime, date, time

currentDict = dict()
oldKey = None
thisKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        maxValue = max(currentDict.values())
        maxTimes = [k for k in currentDict.keys() if currentDict[k] == maxValue]
        for mt in sorted(maxTimes):
            print "{0}\t{1}".format(oldKey, mt)
        currentDict = dict()

    oldKey = thisKey
    time = datetime.strptime(thisValue.split(".")[0], "%Y-%m-%d %H:%M:%S")
    if time.hour not in currentDict:
        currentDict[time.hour] = 0

    currentDict[time.hour] += 1

if thisKey:
    maxValue = max(currentDict.values())
    maxTimes = [k for k in currentDict.keys() if currentDict[k] == maxValue]
    for mt in sorted(maxTimes):
        print "{0}\t{1}".format(oldKey, mt)
