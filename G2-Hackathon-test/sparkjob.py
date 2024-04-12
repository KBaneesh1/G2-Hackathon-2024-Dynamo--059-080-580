import json
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
from pyspark.sql.types import StructType, StructField, StringType


##############################################################################
#####################preprocess jsonl file####################################

print("hi in sparkjob")
def preprocess_jsonl(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    # Insert newline character after each closing curly brace }
    data = data.replace('}{', '}\n{')

    with open(output_file, 'w') as f:
        f.write(data)

# Example usage
preprocess_jsonl('All_products.jsonl', 'preprocessed_products_website.jsonl')


####################################################################################
############################conversion to json file##################################


import json

def jsonl_to_json(jsonl_file, json_file):
    with open(jsonl_file, 'r') as f:
        jsonl_data = f.readlines()

    json_data = [json.loads(line.strip()) for line in jsonl_data]

    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)

# Example usage
jsonl_to_json('preprocessed_products_website.jsonl', 'ip.json')




#######################################################################################
################################df1 creation ###########################################


spark = SparkSession.builder \
    .appName("job") \
    .getOrCreate()
json_file_path = "ip.json"
df1 = spark.read.option("multiLine", True).json(json_file_path)
df1.cache()
#df1.show()
df1.write.csv("out1.csv", mode="overwrite", header=True)
schema = StructType([
    StructField("name", StringType(), True),
    StructField("self_link", StringType(), True),
    StructField("product_url", StringType(), True)
])

# Read the entire JSON file as a single string
json_string = spark.sparkContext.wholeTextFiles("trip.json").collect()[0][1]

# Parse the JSON string into a DataFrame
df2 = spark.read.json(spark.sparkContext.parallelize([json_string]), schema=schema)

result_df = df1.join(df2, (df1.name == df2.name), "left_anti")

# Show the result
result_df.show()
result_df.write.csv("out_final.csv", mode="overwrite", header=True)
# Stop the SparkSession
spark.stop()
