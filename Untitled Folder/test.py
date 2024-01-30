import requests
from bs4 import BeautifulSoup
url = "https://api.odcloud.kr/api/15071311/v1/uddi:a5158b81-27c7-4151-ba6c-b912a6f13d39"
params = {
    "serviceKey" : "JS7jeuof+pwfeEbRwoql+Wry6jw2GgIJlD3GWpVjjxNvEQSSGIc6HaD90Rg3u48tnw6LVidKVigCK2YAxGc4Hw==",
    "page" : 1,
    "perPage" : 1500
}

res = requests.get(url,params)
print(res.json())

data = res.json()['data']
# print(data[0])

# print("내선--------------------------------")
# for d in data:   
#     if d['호선'] == '2' and d['방향'] == '내선':    
#         print(d['역명'], end=' ')
# print("\n외선--------------------------------")
# for d in data:   
#     if d['호선'] == '2' and d['방향'] == '외선':    
#         print(d['역명'], end=' ')
cnt1=0
cnt2=0
cnt3=0
# 2호선 00b140
for d in data:
    
    if d['호선'] == '2' or d['호선'] == '신정지선' or d['호선'] == '성수지선':
        print(d['역명'])

        
