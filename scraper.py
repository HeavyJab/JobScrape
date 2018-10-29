import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=2596cf07104c4dc489e7a5415c7c9c23')
response = requests.get(url)
print response.json()

