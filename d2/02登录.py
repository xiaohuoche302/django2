import urllib
from urllib import request,parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

loginurl = 'http://www.renren.com/PLogin.do'

data = {
    'email': '13979068674',
    'password': 'hsy777898'
}

#data进行url编码
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(loginurl,data=data,headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))