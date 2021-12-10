from urllib import request
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/joke/index.html"
#res = request.urlopen(url)
#使用headers
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers = {'User-Agent':useragent}
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
#print(res.read().decode('utf-8'))
soup = BeautifulSoup(res, 'html.parser')
#print(soup)
#findAll('tag',attribute) select('tag[attribute]')
action_bar = soup.find_all('div',id='action-bar-container')
#print(action_bar)
tmp_div = action_bar[0].find('div')
print('Other <div>\n',tmp_div)
print()
tmp_a = action_bar[0].find('a')
print('Other <a> \n',tmp_a)
print()
tmp_text_in_a = tmp_a.text
print('Text in <a>\n',tmp_text_in_a)
print()
tmp_url = tmp_a['href']
print('URL:')
print('https://www.ppt.cc'+tmp_url)
print()
