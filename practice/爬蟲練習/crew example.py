from urllib import request

url="http://httpbin.org/get"
res=request.urlopen(url)

#print('res.read:()',res)
#print('res.read():', res.read()) -- 出現b'(bytes型別)
#.decode('utf8)  -- 以utf8解碼輸出成HTML原始碼
print(res.read().decode('utf8')) # --輸出完為json字串



