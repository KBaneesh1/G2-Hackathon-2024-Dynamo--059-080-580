
##############################################################################
#####################preprocess jsonl file####################################


# def preprocess_jsonl(input_file, output_file):
#     with open(input_file, 'r') as f:
#         data = f.read()

#     # Insert newline character after each closing curly brace }
#     data = data.replace('}{', '}\n{')

#     with open(output_file, 'w') as f:
#         f.write(data)

# # Example usage
# preprocess_jsonl('products_website.jsonl', 'preprocessed_products_website.jsonl')


####################################################################################
############################conversion to json file##################################


# import json

# def jsonl_to_json(jsonl_file, json_file):
#     with open(jsonl_file, 'r') as f:
#         jsonl_data = f.readlines()

#     json_data = [json.loads(line.strip()) for line in jsonl_data]

#     with open(json_file, 'w') as f:
#         json.dump(json_data, f, indent=4)

# # Example usage
# jsonl_to_json('preprocessed_products_website.jsonl', 'ip.json')




#######################################################################################
################################df creation ###########################################



from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Load JSON into DataFrame") \
    .getOrCreate()
json_file_path = "ip.json"
df = spark.read.option("multiLine", True).json(json_file_path)
df.cache()
df.show()
df.write.csv("out1.csv", mode="overwrite", header=True)
# # Example operation to demonstrate caching
# # Filter the DataFrame to only show rows where the name is "Jira"
# jira_df = df.filter(df.name == "Jira")
# # Show the filtered DataFrame
# jira_df.show()
