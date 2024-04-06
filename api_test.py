import requests
import json
import pandas as pd

api_token = '02331e80c03f428c7b13e12adeea9e4c0164edaeb6c67fcefc8daef0ad93a5b5'
url = 'https://data.g2.com/api/v1/products/'
headers = {
    'Authorization': 'Bearer {0}'.format(api_token)
}

resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    data = resp.json()

    df = pd.DataFrame(data['data'])
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)

    # Display the DataFrame
    print(df)
    # Writing JSON data to a file with indentation of 4
    with open('response_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON response saved to response_data.json")
else:
    print("Failed to retrieve valid response from the API")
