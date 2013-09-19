#!/usr/bin/env python3
#KMeansReduce.py

import sys

(last_Center, sumOfProperty) = ([], [])
sizeOfSameCenter = 0
for line in sys.stdin:
    (center, p) = line.strip('[] \n').split("\t")
    p = [float(i) for i in p.strip('[] ').split(',')]
    
    if last_Center and last_Center != center:
        avgProperty = [i / sizeOfSameCenter for i in sumOfProperty]
        print('%s'%(avgProperty), end = ', ')

        (last_Center, sumOfProperty) = (center, p)
        sizeOfSameCenter = 1
    elif not(last_Center):
        sumOfProperty = [float(i) for i in center.strip('[] ').split(',')]
        last_Center = center
        sumOfProperty =  [(sumOfProperty[i] + p[i]) for i in range(0, len(p))]
        sizeOfSameCenter = sizeOfSameCenter + 1
    else:
        sumOfProperty =  [(sumOfProperty[i] + p[i]) for i in range(0, len(p))]
        sizeOfSameCenter = sizeOfSameCenter + 1

avgProperty = [i / sizeOfSameCenter for i in sumOfProperty]
print(avgProperty)
