import urllib
from urllib import request,parse
import json
from http import cookiejar
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

proxy = {
    "http":"10.3.133.25:808"
}

#创建处理器
proxu_handler = urllib.request.ProxyHandler(proxy)

#打开器
opener = urllib.request.build_opener(proxu_handler)

response = opener.open('http://www.baidu.com/')

print(response.read().decode('utf-8'))