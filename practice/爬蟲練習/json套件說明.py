import requests
import json

url ="https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=236478333"
res = requests.get(url)
# res.text為str
json_str = res.text
# 利用JSON套件 轉換 res.text成dics or list
json_data = json.loads(json_str)
# print(type(json_data)) #得知json_data轉成list
# for d in json_data:    以迴圈方式取得，取得為set
#     print(d)
for k in json_data[0]:    #以迴圈方式取得set中的key值
    print(k)
    