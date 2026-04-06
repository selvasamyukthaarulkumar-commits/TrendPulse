import requests
import json
import time
import os
from datetime import datetime

# get ids
link = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(link)
id_data = r.json()
headers = {"User-Agent": "TrendPulse/1.0"}

# take some ids
ids = id_data[:500]

final_output = []

# category function
def check_category(title):
    title = title.lower()

    if "ai" in title:
        return "technology"
    if "tech" in title:
        return "technology"
    if "war" in title:
        return "worldnews"
    if "game" in title:
        return "sports"
    if "space" in title:
        return "science"
    if "movie" in title:
        return "entertainment"

    return "others"

# loop each id
count = 0

for story_id in ids:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(story_id) + ".json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data is not None:
            if "title" in data:
                cat = check_category(data["title"])

                one = {}
                one["post_id"] = data.get("id")
                one["title"] = data.get("title")
                one["category"] = cat
                one["score"] = data.get("score")
                one["author"] = data.get("by")

                final_output.append(one)

    count = count + 1
    print("Fetching stories:" , count)

# delay set time
    if count % 20 == 0:
        time.sleep(2)

# create folder
if not os.path.exists("data"):
    os.mkdir("data")

# save file as json
today = datetime.now().strftime("%Y%m%d")
name = "data/trends_" + today + ".json"

f = open(name, "w")
json.dump(final_output, f)
f.close()

print("Process completed.")
print(" Collected , Total:", len(final_output),"stories")