from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
from pyspark.sql.types import StructType, StructField, StringType


spark = SparkSession.builder \
    .appName("Load JSON into DataFrame") \
    .getOrCreate()
json_file_path = "ip.json"
df1 = spark.read.option("multiLine", True).json(json_file_path)
df1.cache()
df1.show()
df1.write.csv("out1.csv", mode="overwrite", header=True)



# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Load JSON to DataFrame") \
    .getOrCreate()

# Define the schema of the JSON data
schema = StructType([
    StructField("name", StringType(), True),
    StructField("self_link", StringType(), True),
    StructField("product_url", StringType(), True)
])

# Read the entire JSON file as a single string
json_string = spark.sparkContext.wholeTextFiles("trip.json").collect()[0][1]

# Parse the JSON string into a DataFrame
df2 = spark.read.json(spark.sparkContext.parallelize([json_string]), schema=schema)

# Show the DataFrame to verify the data
df2.show()


spark = SparkSession.builder \
    .appName("DataFrame Difference") \
    .getOrCreate()

# Assuming df1 and df2 are your DataFrames
# df1 is the DataFrame with columns: name, product_link, website_link
# df2 is the DataFrame with columns: name, self_link, product_url

# Perform a left anti join to find rows in df1 that are not in df2
result_df = df1.join(df2, df1.name == df2.name, "left_anti")

# Show the result
result_df.show()

# Stop the SparkSession
spark.stop()
