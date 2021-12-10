from types import TracebackType
import pymysql
import requests
import json
try:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20211001&stockNo=0050"
    res = requests.get(url,headers=headers)
    json_datas = json.loads(res.text)

    print(json_datas['title'].split(" ")[2],json_datas['fields'])
    for x in json_datas['data']:
        x.insert(0,'0050')
        print(x)
except KeyError:
    print("a1")
    pass
except TracebackType:
    print("a")
    pass


# db_settings = {"host": "127.0.0.1","port": 3306,"user": "root","password": "000000","db": "stock","charset": "utf8"}
# try:
#     conn = pymysql.connect(**db_settings)
    
#     with conn.cursor() as cursor:
#         sql = """INSERT INTO market(股票代碼,日期,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#         for stock in json_datas['data']:
#             cursor.execute(sql, stock)
#         conn.commit()

# except Exception as ex:
#     print("Exception:", ex)