import urllib
from urllib import request,parse
import json
from http import cookiejar
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

#创建cookie对象

filename = 'zfcdsn.txt'

cookie = cookiejar.LWPCookieJar(filename)

#处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#打开器
opener = urllib.request.build_opener(cookie_handler)

data = {
    "gps":"",
    "username":"13979068674",
    "password":"T-MAC.35S13P",
    "rememberMe":"true",
    "lt":"LT-439208-2BSZu7eQ9Bjm5vO62N3hKGuGfzjJPK",
    "execution":"e1s1",
    "fkid":"WHJMrwNw1k/F/Zf3AruXHYEvipzaPNtJdsAjxCGjODeKTkzUxCCLpD6DRNHdmqpVeDd2ixa7PNrGr9oW3kXrbwyW9jTG2myjGKFIGZVHdUBAqJF2IpT1xmFm6zjYEzmcwh4fYDLZBqbqyFwtOaSBhyT9yq5crNGFBwYFzTtZV7WhSSvysq30KNhuA8supfd7pTy6C61zgOfWrWKDSO0H3+jNMo2i4NbfOWFqCZ77V38o7agUM2kiEZf71vF5d0CXfsrmt+GiV/7R9QaAioK5ItA==1487582755342",
    "_eventId":"submit",
}

#url编码
data = urllib.parse.urlencode(data).encode('utf-8')

loginUrl = 'https://passport.csdn.net/account/verify'
req = urllib.request.Request(loginUrl,data=data,headers=headers)

response = opener.open(req)

print(response.read().decode('utf-8'))

time.sleep(1)