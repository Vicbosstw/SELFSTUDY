from selenium.webdriver import Chrome
import time

driver = Chrome('./chromedriver_win32/chromedriver')
url = "https://www.dcard.tw/f/"

driver.get(url)
time.sleep(3)

# 搜尋輸入關鍵字
driver.find_element_by_tag_name('input').send_keys('攝影')
time.sleep(5)
# 自動按下搜尋
# driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button').click()
driver.find_element_by_tag_name('input').send_keys(u'\ue007')
time.sleep(3)
# 自動滾動頁面
driver.execute_script('var s = document.documentElement.scrollTOP=5000')
time.sleep(5)
driver.execute_script('var s = document.documentElement.scrollTOP=0')
time.sleep(5)
driver.execute_script('var s = document.documentElement.scrollTOP=10000')
time.sleep(5)
html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")
print(html)
time.sleep(5)
driver.close()
