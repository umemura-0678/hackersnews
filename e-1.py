import requests
import time

new_id_list = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
# print(new_id_list)
for i in range(30):
    # データ取得
    data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{new_id_list[i]}.json?print=pretty").json()
    
    if data.get("url") is None:
        data["url"] = "None"

    result_dict = {"title": data["title"], "link": data["url"]}
    print(result_dict)

    time.sleep(1)

