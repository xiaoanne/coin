# coding: utf-8
import requests
import json

# Set up the request parameters
host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

# Define the API endpoint and query parameters
url = '/spot/currencies'
query_param = ''

# Make the GET request
r = requests.request('GET', host + prefix + url, headers=headers)

with open('output/currencies.json', 'w', encoding='utf-8') as json_file:
    json.dump(r.json(), json_file, ensure_ascii=False, indent=4)  # Save JSON with indentation

# Parse the response
data = r.json()

# Extract only the "currency" values from each object in the response
currencies = [item['currency'] for item in data]

# Print the list of currencies
print(currencies)

# Save the list of currencies to a JSON file
with open('output/currencies_list.json', 'w', encoding='utf-8') as json_file:
    json.dump(currencies, json_file, ensure_ascii=False, indent=4)
