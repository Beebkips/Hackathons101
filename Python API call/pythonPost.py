import requests
r = requests.post('my.url.com', json={"key", "value"})
print(r.json())