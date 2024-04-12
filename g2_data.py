import requests
import json
import pandas as pd

api_token = '02331e80c03f428c7b13e12adeea9e4c0164edaeb6c67fcefc8daef0ad93a5b5'
url = 'https://data.g2.com/api/v1/products/'
headers = {
    'Authorization': 'Bearer {0}'.format(api_token)
}

all_products = []
count = 0
next_page_url = url

while next_page_url:
    try:
        resp = requests.get(next_page_url, headers=headers)
        if resp.status_code == 200:
            arr = []
            data = resp.json()

            in_data  = data["data"]
            # print(type(data))
            name = None
            self_link  =None
            prod_url = None
            for prod in (in_data):
                name = prod["attributes"]["name"]
                # print(name)
                self_link = prod["links"]["self"]
                prod_url = prod["attributes"]
                new_data = {
                    "name":name,
                    "self_link":self_link
                }
                # print(new_data)
                all_products.append(new_data)
            print(count)
            next_page_url = data['links'].get('next')
        else:
            print("Failed to retrieve valid response from the API")
            break
        count += 1
    except Exception as e:
        print(e)
        break


# Display the DataFrame
# print(df)
 # df = pd.DataFrame(all_products)
        # pd.set_option('display.max_columns', None)
                # pd.set_option('display.expand_frame_repr', False)
            # pd.set_option('max_colwidth', None)
# Writing JSON data to a file with indentation of 4
with open('trip.json', 'w') as json_file:
    json.dump(all_products, json_file, indent=4)

print("JSON response saved to response_data.json")

# i gave got 10 pag