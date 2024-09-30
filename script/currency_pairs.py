# coding: utf-8
import requests
import json

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/currency_pairs'
query_param = ''
r = requests.request('GET', host + prefix + url, headers=headers)

with open('output/currency_pair.json', 'w', encoding='utf-8') as json_file:
    json.dump(r.json(), json_file, ensure_ascii=False, indent=4)  # Save JSON with indentation


# Parse the response
data = r.json()

# Extract only the "currency" values from each object in the response
currencies = [item['id'] for item in data]

# Print the list of currencies
print(currencies)

# Save the list of currencies to a JSON file
with open('output/currencies_pair_list.json', 'w', encoding='utf-8') as json_file:
    json.dump(currencies, json_file, ensure_ascii=False, indent=4)

# Filter the list to keep only strings ending with '_USDT'
usdt_currencies = [currency for currency in currencies if currency.endswith('_USDT')]

# Print the filtered list
print(usdt_currencies)

# Save the filtered list to a JSON file
with open('output/usdt_currencies.json', 'w', encoding='utf-8') as json_file:
    json.dump(usdt_currencies, json_file, ensure_ascii=False, indent=4)