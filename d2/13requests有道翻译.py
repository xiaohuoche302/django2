import urllib
from urllib import request,parse
import json
from http import cookiejar
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
#去掉_o
ydurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {
    "i":" 人才",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1534254789170",
    "sign":"414216dda392a19fb9a23e553d0aa607",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false",
}

ydresponse = requests.post(ydurl, data=data, headers=headers)
print(ydresponse.text)
data = json.loads(ydresponse.text)['translateResult'][0]
print(data)

# .json() 转为字典
print(ydresponse.json()['translateResult'][0])
