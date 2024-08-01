import requests

URL = "http://google.com"

response = requests.get(URL)

if response.status_code == 200:
    print("Site available")
else:
    print("Error")