from types import TracebackType
import requests
import json
import pymysql
import time
import random
from fake_useragent import UserAgent

class Stock:
    # 建構式
    def __init__(self,*stock_numbers):
        self.stock_numbers = stock_numbers
        # print(self.stock_numbers)

    # 爬取
    
    def scrape_save(self):        
        db_settings = {"host": "127.0.0.1","port": 3306,"user": "root","password": "000000","db": "stock","charset": "utf8"} #mysql連線設定
        yr = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'] #網址年份
        month = ['01','02','03','04','05','06','07','08','09','10','11','12'] #網址月份
        user_agents = UserAgent() #偽裝headers
        delay_choices = [5,7,4,9,3,2,1,4,5] #隨機取數
        delay = random.choice(delay_choices)
        try:
            for one_year in yr:
                for one_month in month:
                    for stock_number in self.stock_numbers:
                        response = requests.get(
                            "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+(one_year)+(one_month)+"01&stockNo="+(stock_number),
                            headers={'User-Agent':user_agents.random})
                        json_datas = json.loads(response.text)
                        time.sleep(3)
                        for x in json_datas['data']:
                            x.insert(0,stock_number)     
                            print(x)
                            # time.sleep(1)                                
                        try:
                            conn = pymysql.connect(**db_settings)
                            
                            with conn.cursor() as cursor:
                                sql = """INSERT INTO market(股票代碼,日期,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                                for stock in json_datas['data']:
                                    cursor.execute(sql,stock)
                                conn.commit()

                        except Exception as ex:
                            print("Exception:",ex)
        except KeyError:
            pass
        except TracebackType:
            pass
        with conn.cursor() as cursor:
            sql_code = """INSERT INTO marketcode(股票名稱,股票代碼) VALUES(%s,%s)"""
            marketcode = [json_datas['title'].split(" ")[2],stock_number]
            cursor.execute(sql_code,marketcode)
            conn.commit()
            print("Completed")
stock = Stock('0050')
stock.scrape_save()
input("Press Enter to exit")
