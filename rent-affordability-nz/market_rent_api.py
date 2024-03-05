import requests
import json
import yaml

url = "https://api.business.govt.nz/gateway/tenancy-services/market-rent/v2/statistics?period-ending=2023-12&num-months=12&area-definition=REGC2019"

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")

headers = {
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': data['api_key'],
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Parse JSON response directly
        print(json.dumps(data, indent=4))   # Print the parsed JSON data
        api = pd.read_json(data)
    else:
        print(f"Error: API request failed with status code {response.status_code}")
except Exception as e:
    print(f"An exception occurred: {e}")

api = pd.DataFrame(data["items"])
api.to_csv('rent_api_data.csv', index=False)