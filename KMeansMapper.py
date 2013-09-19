#!/usr/bin/env python3
# KMeansMapper.py

import sys
import linecache
import random
centerList = [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]

def distanceOfTwoProperty(property1, property2):
    temp = [(property1[i] - property2[i]) ** 2 for i in range(0, len(property1))]
    return sum(temp)

for line in sys.stdin:
    val = [float(i) for i in line.strip().split()]
    minDistance = distanceOfTwoProperty(val, centerList[0])
    minCenter = centerList[0]
    
    for i in range(1, len(centerList)):
        dist = distanceOfTwoProperty(val, centerList[i])
        if dist < minDistance:
            minCenter = centerList[i]
            minDistance = dist
    print('%s\t%s'%(minCenter, val))
        
