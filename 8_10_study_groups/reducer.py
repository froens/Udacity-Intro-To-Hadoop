#!/usr/bin/python

import sys
from datetime import datetime, date, time

currentList = []
oldKey = None
thisKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, currentList)
        currentList = []
   
    oldKey = thisKey

    currentList.append(thisValue)

if thisKey:
    print "{0}\t{1}".format(oldKey, currentList)
