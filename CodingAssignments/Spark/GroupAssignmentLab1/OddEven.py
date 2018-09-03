from pyspark import SparkConf, SparkContext
from pyspark.mllib.stat import Statistics

APP_NAME = "My Spark Application"
NTIMES = 30000


def oddeven(sc):
        odds = []
        for i in range(1, NTIMES, 2):
                odds.append(i)

        evens = []
        for i in range(2, NTIMES, 2):
                evens.append(i)

        rddodds = sc.parallelize(odds)
        rddevens = sc.parallelize(evens)
        #print(rddodds.collect())
        #print(rddevens.collect())

        rddoddspair = rddodds.map(lambda x: (x, "a" * x))
        rddevenspair = rddevens.map(lambda x: (x, "b" * x))
        #print(rddoddspair.collect())
        #print(rddevenspair.collect())

        allkeys = rddoddspair.keys().union(rddevenspair.keys())
        #print(allkeys.collect())

        #calculate the statistics now
        summary = allkeys.stats()
        print("\n****Printing summary stats of all the keys****")
        print("(count: " + str(summary.count()) + ", mean: " + str(summary.mean()) + ", stdev: " + str(summary.stdev()) + ", max: " + str(summary.max()) + ", min: " + str(summary.min()) + ")")

        # Now calculate the summary stats of the first 100 numbers and their stats;
        summary = sc.parallelize(allkeys.take(100)).stats() # This method works but we dont really need to paralleize and create another RDD, because now the datasize is very small and with the driver program; it would be more efficient to call some other common fucntion to get statistics.
        print("\n****Printing summary stats of first 100 items****")
        print("(count: " + str(summary.count()) + ", mean: " + str(summary.mean()) + ", stdev: " + str(summary.stdev()) + ", max: " + str(summary.max()) + ", min: " + str(summary.min()) + ")")
	

if __name__ == "__main__":
        # Configure Spark
        conf = SparkConf().setAppName(APP_NAME)
        conf = conf.setMaster("local[*]")
        sc   = SparkContext(conf=conf)
        oddeven(sc)
	sc.stop()


