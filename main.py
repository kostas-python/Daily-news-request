import requests
import json

api_key = "b64e47ba730746dd988f986a5b38add8"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-08-19&sortBy=publishedAt&apiKey=" \
    "b64e47ba730746dd988f986a5b38add8"

request = requests.get(url)
content = request.text
print(content)