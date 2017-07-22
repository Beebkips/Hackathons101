import requests, json

APICall = requests.get('https://catfact.ninja/fact')
getJson = json.loads(APICall.text)
print(getJson)