import requests
from send_email import send_email

topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}"
       "&apiKey=8559cc8f40fc43a1a7e4d254130a82ea"
       "&language=en")

# Get the JSON from the News API
r = requests.get(url)
content = r.json()

# Create a message to be sent through email
message = f"""\
Subject: News Update
\nShowing {content['totalResults']} articles...
"""

# Include every articles title, author, url, and description
for i in content["articles"]:

    # Check to see if a title exists
    if i["title"] is not None:
        message += "\n" + i["title"]
    else:
        message += "\n" + "*Title not found*"

    # Check to see if an author exists
    if i["author"] is not None:
        message += "\n" + i["author"]
    else:
        message += "\n" + "*Author not found*"

    # Check to see if an url exists
    if i["url"] is not None:
        message += "\n" + i["url"]
    else:
        message += "\n" + "*URL not found*"

    # Check to see if a description exists
    if i["description"] is not None:
        message += "\n" + i["description"] + "\n"
    else:
        message += "\n" + "*Description not found*" + "\n"

# Encode to utf-8 and send the email
send_email(message.encode('utf-8'))
