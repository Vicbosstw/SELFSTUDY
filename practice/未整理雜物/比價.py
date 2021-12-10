from requests import request
from requests import get

url = "https://www.104.com.tw/jobs/search/list?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page=1&mode=s&jobsource=2018indexpoc"
headers = {"Referer":"https://www.104.com.tw/jobs/search/?keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%B8%AB&order=1&jobsource=2018indexpoc&ro=0",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
res = get(url,headers=headers)

print(res.text)