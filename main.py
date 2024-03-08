import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8559cc8f40fc43a1a7e4d254130a82ea"

# Get the JSON from the News API
r = requests.get(url)
content = r.json()

# Display total number of articles
print(f"\nShowing {content['totalResults']} articles...\n")

# Display the title, author, url and description for each article
for i in content["articles"]:
    print(i["title"])
    print(i["author"])
    print(i["url"])
    print(i["description"])
    print()
