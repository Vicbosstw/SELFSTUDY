import requests
import json

from requests.api import head
from urllib import request
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=236478651"

res_path = r'./dcard_photography'
if not os.path.exists(res_path):
    os.mkdir(res_path)

for i in range (1,3):
    

res = requests.get(url,headers=headers)
json_str = res.text
json_data = json.loads(json_str)
last_id = json_data[len(json_data)-1]['id']
for each_article in json_data:
    print(each_article['title'])
    print('https://www.dcard.tw/f/photography/p/'+str(each_article['id']))
    print()
    for n, img_url in enumerate(each_article['mediaMeta']):
        tmp_img_url = img_url['url']
        location = os.path.join(res_path + '/%s_%s.jpg'%(each_article['title'].replace('/',''),n))
        print(('\t'+tmp_img_url))
        request.urlretrieve(tmp_img_url,location)
        print('\tDone.')

    print("換頁".center(40,"-"))

url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before={}".format(last_id)
