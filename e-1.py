import requests
import time

new_id_list = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
#print(new_id_list)
for i in range(30):
    # データ取得
    data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{new_id_list[i]}.json?print=pretty" ).json()
    try:
        data["url"]
    except Exception as e:
        data["url"]="None"
    finally:
        dict = {"title":data["title"],"link": data["url"]}
        print(dict)
        
    time.sleep(1)

# 出力
# {'title': 'PYX: The next step in Python packaging', 'url': 'https://astral.sh/pyx'}
# {'title': 'Nginx introduces native support for ACME protocol', 'url': 'https://blog.nginx.org/blog/native-support-for-acme-protocol'}
# {'title': 'FFmpeg 8.0 adds Whisper support', 'url': 'https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/13ce36fef98a3f4e6d8360c24d6b8434cbb8869b'}
# {'title': 'OCaml as my primary language', 'url': 'https://xvw.lol/en/articles/why-ocaml.html'}
# {'title': 'Pebble Time 2* Design Reveal', 'url': 'https://ericmigi.com/blog/pebble-time-2-design-reveal/'}
