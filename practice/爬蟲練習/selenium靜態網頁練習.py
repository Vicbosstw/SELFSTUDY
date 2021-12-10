from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup

driver = Chrome('C:\Program Files\Google\Chrome\Application\chrome.exe')
url =('https://www.ptt.cc/bbs/index.html')
driver.get(url)
# driver.find_element_by_class_name('board-name').click()
# driver.find_element_by_class_name('btn-big').click()

# cookie = driver.get_cookies()
# driver.close()

# # 設定cookies
# ss = requests.session()
# for c in cookie:
#     ss.cookies.set(c['name'],c['value'])
# res = ss.get("https://www.ptt.cc/bbs/Gossiping/index.html")
# soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
