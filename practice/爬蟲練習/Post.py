#from urllib import request, parse
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = "http://httpbin.org/post"
data = {'key1':'value1', 'key2':'value2'}
res = requests.post(url, data=data, headers=headers)
#data =bytes(parse.urlencode(data), encoding='utf-8') urllib 需轉成二進制
#req = request.Request(url = url, data = data , headers=headers)
#res = request.urlopen(req).read().decode('utf-8')
#soup = BeautifulSoup(res,'html.parser')
soup = BeautifulSoup(res.text,'html.parser')
print(soup.prettify())