import findspark

findspark.init()

import pyspark

sc = pyspark.SparkContext(master='spark://spark-master:7077')

iteration=10000000

partition=4

data = range(0,iteration)

distIn = sc.parallelize(data,partition)

result=distIn.map(lambda n:(1 if n%2==0 else -1)/float(2*n+1)).reduce(lambda a,b: a+b)

f = open("/opt/spark-data/result.txt","w+")
f.write(str(result*4))
f.close() 
