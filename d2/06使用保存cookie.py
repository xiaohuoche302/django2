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
cookie = cookiejar.LWPCookieJar()
#运用已保存在renren.txt文件中的cookie数据来进行打开，不在需要填写登录信息(data)
cookie.load(filename,ignore_expires=True,ignore_discard=True)

#处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#打开器
opener = urllib.request.build_opener(cookie_handler)

req = urllib.request.Request('http://www.renren.com/967457216/profile',headers=headers)

response = opener.open(req)

print(response.read().decode('utf-8'))