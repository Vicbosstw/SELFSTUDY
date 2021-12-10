from functools import partialmethod
from bs4.builder import PERMISSIVE
import requests
from bs4 import BeautifulSoup

url_target = 'https://webtest.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'
#post data
post_data_str = '''method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/07/06
awardAnnounceEndDate: 110/07/06
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢'''
post_data= {}
for row in post_data_str.split('\n'):
    post_data[row.split(': ')[0]] = row.split(': ')[1]
headers_str = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 429
Content-Type: application/x-www-form-urlencoded
Cookie: cookiesession1=5135051BYTLVB1YTJGMHJXOCTOU009CB; JSESSIONID=0000QhayxZyBeJv-N8ej-zMZoJz:14obonkfs; NSC_xfcuftu_qfstjtufodf=ffffffff09081f6445525d5f4f58455e445a4a423660
Host: webtest.pcc.gov.tw
Origin: https://webtest.pcc.gov.tw
Referer: https://webtest.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'''
headers = {}
for row in headers_str.split('\n'):
    headers[row.split(': ')[0]] = row.split(': ')[1]

res = requests.post(url_target, headers=headers, data = post_data)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)
title = soup.select('div[id="print_area"] td[align="left"]')
for n, i in enumerate(title):
    if(n+1)%4 == 2:
        print(i.u.text)
    else:
        print(i)
    if (n+1) % 4 == 0:
        print('='*20)