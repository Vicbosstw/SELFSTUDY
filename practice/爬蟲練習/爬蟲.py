import requests
from bs4 import BeautifulSoup
import os

from soupsieve.css_match import REL_SIBLING

resource_path = './res'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup.prettify())
article_title_html = soup.select('div[class="title"]')
print(article_title_html)
# for each_article in article_title_html:
#     try:
#         print(each_article.a.text) 
#         print('https://www.ptt.cc'+each_article.a['href'])
#         article_url = 'https://www.ptt.cc'+each_article.a['href']
#         article_text = each_article.text
#         article_res = requests.get(article_url, headers=headers)
#         article_soup = BeautifulSoup(article_res.text,'html.parser')
#         article_content = article_soup.select('div[id="main-content"]')[0].text.split('--')[0]
#         print(article_content)
#         with open(r'%s/%s.txt' % (resource_path,article_text), 'w', encoding='utf-8') as w:
#             w.write(article_content)
#     except AttributeError:
#         pass
    
 