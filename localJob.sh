#!/bin/bash
# job.sh

for i in {1..50}
do
	echo $i
	res=`cat iris.data |./KMeansMapper.py |sort|./KMeansReduce.py`
	echo '['$res']'
	echo '['$res']' >> c.data
	sed -i "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
done
