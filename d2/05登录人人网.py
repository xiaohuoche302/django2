import urllib
from urllib import request,parse
import json
from http import cookiejar
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

#创建cookie对象
filename = 'renren.txt'
cookie = cookiejar.LWPCookieJar(filename)

#处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#打开器
opener = urllib.request.build_opener(cookie_handler)

loginurl = 'http://www.renren.com/PLogin.do'

data =  {
    'email': '13979068674',
    'password': 'hsy777898'
}

#url编码
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(loginurl,data=data,headers=headers)

response = opener.open(req)

print(response.read().decode('utf-8'))

cookie.save(ignore_discard=True,ignore_expires=True)


#跳转到个人主页
url = 'http://www.renren.com/967457216/profile'
#因为获取了cookie，所以可以通过打开器直接打开
profileRes = opener.open(url)

print(profileRes.read().decode('utf-8'))

print(profileRes.url)