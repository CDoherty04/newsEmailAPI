import requests
from send_email import send_email

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8559cc8f40fc43a1a7e4d254130a82ea"

# Get the JSON from the News API
r = requests.get(url)
content = r.json()

# Create a message to be sent through email
message = f"""\
Subject: News Update
\nShowing {content['totalResults']} articles...
"""

for i in content["articles"]:
    # Include every articles title, author, url, and description
    message += "\n" + i["title"]
    message += "\n" + i["author"]
    message += "\n" + i["url"]
    message += "\n" + i["description"] + "\n"

# Encode to utf-8 and send the email
send_email(message.encode('utf-8'))
