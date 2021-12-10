from re import L
from bs4.element import SoupStrainer
import requests
import json
from bs4 import BeautifulSoup

url = "https://buzzorange.com/techorange/"
url_post = "https://buzzorange.com/techorange/wp-admin/admin-ajax.php"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
for page in range(0,10):
    post_data = {"action":"fm_ajax_load_more","nonce":"0350e1a106","page": page + 1}

    res = requests.post(url_post,headers=headers,data=post_data)
    data_dict = json.loads(res.text)

    # print(data_dict["success"])----回傳True
    # print("="*20)
    # print(data_dict["data"])------下頁HTML

    html = data_dict["data"]
    soup = BeautifulSoup(html,"html.parser")
    for i in soup.select("h4 a"):
        print(i.text)
        print(i["href"])
        print()
