import requests
import json
import pandas as pd

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=IPHONE12&page=1&sort=sale/dc"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}

res = requests.get(url,headers=headers)
json_string = json.loads(res.text)
prodids = []
print(json_string)
names =[]
for prodid in json_string['prods']:
    prodids.append(prodid['Id'])
    names.append(prodid['name'])
prodids = list(set(prodids))
names = list(set(names))
# print(prodids)
price = []
price_cleaner = []
qty = []
price_url = "https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id={}&fields=Id,Price,Qty".format(','.join(prodids))
# print(price_url)
price_jres = requests.get(price_url,headers=headers)
price_json = json.loads(price_jres.text)
for k in price_json:
    k['Id'] = k['Id'].split('-0')[0]
    if k['Id'] not in price_cleaner:
        price_cleaner.append(k['Id'])
        price.append(k['Price']['P'])
        qty.append(k['Qty'])
htmls = []
for i in prodids:
    htmls.append("https://24h.pchome.com.tw/prod/"+i)
if prodids == price_cleaner:
    df_ID = pd.DataFrame(prodids,columns=['ID'])
    df_Name = pd.DataFrame(names,columns=['Title'])
    df_price = pd.DataFrame(price,columns=['price'])
    df_qty = pd.DataFrame(qty,columns=['qty'])

    df = pd.DataFrame(
        {'ID':prodids,
        'Title':names,
        'Price':price,
        'Qty':qty,
        'Html':htmls}
    )
    df.to_excel('excel_output.xlsx',sheet_name='Sheet1')
print(df)
    