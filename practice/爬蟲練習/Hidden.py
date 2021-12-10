import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://webtest.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.select('input[type="hidden"]'):
    try:
        print('%s:\t%s'%(i['name'],i['value']))
    except KeyError:
        pass
