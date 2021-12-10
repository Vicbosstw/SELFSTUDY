import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from fake_useragent import UserAgent

keywords = [
    'ode','odf','odd',
    'odg','odh','odz','ofa','ofb','ofc','ofd','ofe','off','ofg','ofh','ofi','ofz','oba','obb','obf','obd','obe','obc','obz','oha','ohi','ohj','ohk','ohh','ohg','ohb','ohc','ohd',
    'ohe','ohf','ohz','oia','oib','oic','oid','oie','oig','oih','oii','oij','oik','oil','oim','oiz','oja','ojd','ojc','ojb','ojz','oaa','oaf','oae','oad','oac','oab','oca','ocb',
    'occ','ocd','oce','ocf','ocg','oea','oeb','oea','oec',
]
ua = UserAgent()
user_agent = ua.random
for keyword in keywords:   
    kurl = "https://www.kingstone.com.tw/book/{}".format(keyword)
    page = 0
    article = [0]
    book_np = 0
    while not article == [] :
        try:
            page += 1
            url = kurl+"?&page={}".format(str(page))
            headers = {'User-Agent': user_agent}
            res = requests.get(url,headers=headers)
            soup = BeautifulSoup(res.text,"html.parser")
            article = soup.select('h3[class="pdnamebox"] a')
        except:
            page += 1
            url = kurl+"?&page={}".format(str(page))
            headers = {'User-Agent': user_agent}
            res = requests.get(url,headers=headers)
            soup = BeautifulSoup(res.text,"html.parser")
            article = soup.select('h3[class="pdnamebox"] a')
        if article != []:
            for k,i in enumerate (article):
                book =list()
                book_intros = list()
                # book_name = i.text
                book.append(i.text)
                book_html = "https://www.kingstone.com.tw/"+i['href']
                book.append(book_html)
                book_res = requests.get(book_html,headers=headers)
                book_soup = BeautifulSoup(book_res.text,"html.parser")
                book.append(book_soup.select('li[class="basicunit"] a')[0].text)
                if book_soup.select('li[class="basicunit"] a')[2].text == '?':
                    book.append(book_soup.select('li[class="basicunit"] a')[3].text)
                else:
                    book.append(book_soup.select('li[class="basicunit"] a')[2].text)
                book.append(book_soup.select('div[class="alpha_main"] a')[0]['href'])
                try:
                    book.append(book_soup.select('ul[class="table_2col_deda"]')[1].select('li[class="table_td"]')[1].text)
                    book_intros.append(book_soup.select('ul[class="table_2col_deda"]')[1].select('li[class="table_td"]')[1].text)
                except IndexError:
                    book.append(0)
                    book_intros.append(0)
                try:
                    book_intro = book_soup.select('div[class="pdintro_txt1field panelCon"]')[0]
                    book_intros.append(book_intro.text)
                except IndexError:
                    book_intros.append(0)
                if book_np is 0:
                    book_np = np.array([book])
                    book_intro_np = np.array([book_intros])
                else:
                    book_np = np.vstack([book_np,book])
                    book_intro_np = np.vstack([book_intro_np,book_intros])
                print(k+1,i.text)
                print("Loading.....")
                time.sleep(3)
            
            print("第{}頁".format(page).center(20,"="))
            time.sleep(15)
        else:
            print("OKOKOK")
            break
    df = pd.DataFrame(data=book_np,columns=("書名","書籍網站","作者","出版社","ISBN","圖片網址"))
    df_intro = pd.DataFrame(data=book_intro_np,columns=("ISBN","書籍簡介"))
    df.to_csv("kingstone_{}.csv".format(keyword),encoding="utf-8-sig",index=False)
    df_intro.to_csv("kingstone_{}_intro.csv".format(keyword),encoding="utf-8-sig",index=False)
    print("Completed")
    # time.sleep(5)

    time.sleep(90)


input("Press Enter to exit!")


input("Press Enter to exit!")