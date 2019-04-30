import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext(master='spark://spark-master:7077')
rdd = sc.parallelize(range(1000))
rdd.takeSample(False, 1000)

