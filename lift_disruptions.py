import requests
import pprint
r = requests.get('https://api.tfl.gov.uk/Disruptions/Lifts/')
results = r.json()
for item in results:
    print(item['message'])