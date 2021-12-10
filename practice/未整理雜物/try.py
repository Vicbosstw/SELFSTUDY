import requests
import json
import pymysql
import time
class Stock:
    # 建構式
    def __init__(self,*stock_numbers):
        self.stock_numbers = stock_numbers
        # print(self.stock_numbers)

    # 爬取
    
    def scrape(self):
        yr = ['01','02','03','04','05','06','07','08','09','10','11','12']
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        for one_year in yr:
            for stock_number in self.stock_numbers:
                response = requests.get(
                    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2020"+one_year+"01&stockNo="+stock_number,headers=headers)
                json_datas = json.loads(response.text)
                for x in json_datas['data']:
                    x.insert(0,stock_number)
                    # time.sleep(5)
                    print(x)       
                    db_settings = {"host": "127.0.0.1","port": 3306,"user": "root","password": "000000","db": "stock","charset": "utf8"}
                    try:
                        conn = pymysql.connect(**db_settings)
                        
                        with conn.cursor() as cursor:
                            sql = """INSERT INTO market(股票代碼,日期,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                            for stock in json_datas['data']:
                                cursor.execute(sql,stock)
                            conn.commit()

                    except Exception as ex:
                        print("Exception:", ex)

stock = Stock('2330')
stock.scrape()
