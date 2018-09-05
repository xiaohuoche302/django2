import urllib
from urllib import request,parse
import json
from http import cookiejar
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

#创建cookie对象
filename = 'zbrenren.txt'
cookie = cookiejar.LWPCookieJar(filename)

#处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#打开器
opener = urllib.request.build_opener(cookie_handler)

urllib.request.install_opener(opener)

data = {
    "email":"13979068674",
    "icode":"",
    "origURL":"http://www.renren.com/home",
    "domain":"renren.com",
    "key_id":"1",
    "captcha_type":"web_login",
    "password":"548c27eab6f7ddaadda2bef9cf98c2974719e2714d5d24f73b9edbbb6fd68841",
    "rkey":"af7035a213a55563d74317ecfd26cbef",
    "f":"http%3A%2F%2Fsc.renren.com%2Fscores%2Fmycalendar"
}
#url编码
data = urllib.parse.urlencode(data).encode('utf-8')

loginUrl = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201872205870"

req = urllib.request.Request(loginUrl,data,headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))

time.sleep(1)

print(urllib.request.urlopen('http://www.renren.com/967457216/profile').read().decode('utf-8'))