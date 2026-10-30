from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, DoubleType

spark = SparkSession.builder \
    .appName("SensorStreamingConsumer") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", FloatType()),
    StructField("humidity", FloatType()),
    StructField("timestamp", DoubleType())
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()

parsed = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

query = parsed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()