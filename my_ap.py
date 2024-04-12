# import requests
# import json
# import pandas as pd

# api_token = '02331e80c03f428c7b13e12adeea9e4c0164edaeb6c67fcefc8daef0ad93a5b5'
# url = 'https://data.g2.com/api/v1/products/'
# headers = {
#     'Authorization': 'Bearer {0}'.format(api_token)
# }

# all_products = []
# next_page_url = url

# while next_page_url:
#     try:
#         resp = requests.get(next_page_url, headers=headers)
#         if resp.status_code == 200:
#             data = resp.json()
#             products_on_page = data.get('data', [])
#             for product in products_on_page:
#                 product_info = {
#                     'name': product.get('attributes', {}).get('name', ''),
#                     'product_url': product.get('links', {}).get('self', '')
#                 }
#                 all_products.append(product_info)
#             next_page_url = data['links'].get('next')
#         else:
#             print("Failed to retrieve valid response from the API")
#             break
#     except Exception as e:
#         print(e)
#         break

# # Convert the list of dictionaries into a DataFrame
# df = pd.DataFrame(all_products)

# # Display the DataFrame
# print(df)

# # Writing JSON data to a file with indentation of 4
# with open('respons.json', 'w') as json_file:
#     json.dump(all_products, json_file, indent=4)

# print("JSON response saved to response_data.json")

















# import requests
# import json
# import pandas as pd

# api_token = '02331e80c03f428c7b13e12adeea9e4c0164edaeb6c67fcefc8daef0ad93a5b5'
# url = 'https://data.g2.com/api/v1/products/'
# headers = {
#     'Authorization': 'Bearer {0}'.format(api_token)
# }

# all_products = []
# count = 0
# next_page_url = url

# while next_page_url and count<3:
#     try:
#         resp = requests.get(next_page_url, headers=headers)
#         if resp.status_code == 200:
#             arr = []
#             data = resp.json()

#             in_data  = data["data"]
#             # print(type(data))
#             name = None
#             self_link  =None
#             prod_url = None
#             for prod in (in_data):
#                 name = prod["attributes"]["name"]
#                 # print(name)
#                 self_link = prod["links"]["self"]
#                 prod_url = prod["attributes"]["product_url"]
#                 new_data = {
#                     "name":name,
#                     "self_link":self_link,
#                     "product_url":prod_url
#                 }
#                 print(new_data)
#                 all_products.append(new_data)
#             print(count)
#             next_page_url = data['links'].get('next')
#         else:
#             print("Failed to retrieve valid response from the API")
#             break
#         count += 1
#     except Exception as e:
#         print(e)
#         break


# # Display the DataFrame
# # print(df)
#  # df = pd.DataFrame(all_products)
#         # pd.set_option('display.max_columns', None)
#                 # pd.set_option('display.expand_frame_repr', False)
#             # pd.set_option('max_colwidth', None)
# # Writing JSON data to a file with indentation of 4
# with open('trip.json', 'w') as json_file:
#     json.dump(all_products, json_file, indent=4)

# print("JSON response saved to response_data.json")

# # i gave got 10 pag



from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode
from pyspark.sql.types import StructType, StructField, StringType

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
df = spark.read.json(spark.sparkContext.parallelize([json_string]), schema=schema)

# Show the DataFrame to verify the data
df.show()

# Save the DataFrame to a CSV file
df.write.csv("output.csv", header=True)

# Stop the SparkSession
spark.stop()


