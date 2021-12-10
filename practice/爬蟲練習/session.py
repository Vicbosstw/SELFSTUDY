import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
hearders = {"User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
ss = requests.session()
ss.cookies['over18'] =  '1'
res = ss.get(url, headers=hearders)
print(res.text)