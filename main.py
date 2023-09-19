import requests
from send_email import send_email

api_key = "b64e47ba730746dd988f986a5b38add8"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "b64e47ba730746dd988f986a5b38add8"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n"

body = body.encode("utf-8")
send_email(message=body)


