import requests
from bs4 import BeautifulSoup

headers = {"User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url_landing_page = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
url_tmp = ''
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
data = {}

ss = requests.session()
res_landing_page = ss.get(url_landing_page,headers=headers)
soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')
button = soup_landing_page.select('button[class="btn-big"]')[0]

button_key = button['name']
button_value = button['value']
data[button_key] = button_value

hidden = soup_landing_page.select('input')[0]
hidden_key = hidden['name']
hidden_value = hidden['value']
data[hidden_key] = hidden_value
url_tmp = 'https://www.ptt.cc'+ soup_landing_page.select('form')[0]['action']
ss.post(url_tmp,data=data,headers=headers)
res_index = ss.get(url, headers=headers)
print(res_index.text)
