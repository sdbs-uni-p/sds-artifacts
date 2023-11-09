#!/usr/local/bin/python

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

