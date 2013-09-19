#!/bin/bash
# job.sh
rm c.data
touch c.data
$HADOOP_COMMON_HOME/bin/hadoop fs -rm -R /output
$HADOOP_COMMON_HOME/bin/hadoop jar $HADOOP_COMMON_HOME/share/hadoop/tools/lib/hadoop-streaming-2.0.5-alpha.jar -input /iris.data -mapper /home/hd/workspace/KMeanHadoop/KMeansMapper.py -reducer /home/hd/workspace/KMeanHadoop/KMeansReduce.py -output /output/1
prev=`$HADOOP_COMMON_HOME/bin/hadoop fs -cat /output/1/part-00000`
sed -i "7s/^.*$/centerList\ = [$prev]/" KMeansMapper.py

for i in {2..50}
do
	echo $i
	$HADOOP_COMMON_HOME/bin/hadoop jar $HADOOP_COMMON_HOME/share/hadoop/tools/lib/hadoop-streaming-2.0.5-alpha.jar -input /iris.data -mapper /home/hd/workspace/KMeanHadoop/KMeansMapper.py -reducer /home/hd/workspace/KMeanHadoop/KMeansReduce.py -output /output/$i
	res=`$HADOOP_COMMON_HOME/bin/hadoop fs -cat /output/$i/part-00000`
	if [ "$res" = "$prev" ]
	then
		echo "Have been done! The Center is found!"
		break
	else
		prev=$res
		echo '['$res']'
		echo '['$res']' >> c.data
		sed -i "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
	fi
done
