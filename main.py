import requests
from send_email import send_email

topic = "tesla"

api_key = "b64e47ba730746dd988f986a5b38add8"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&apiKey=" \
    "b64e47ba730746dd988f986a5b38add8&" \
    "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" "\n"

for article in content["articles"][:20]:

    title = article.get("title", "")
    description = article.get("description", "")
    url = article.get("url", "")

    body += f"{title}\n{description}\n{url}\n\n"

body = body.encode("utf-8")
send_email(message=body)