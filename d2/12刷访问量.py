import urllib
from urllib import request
import random

proxies = [
    {'https':'171.39.3.241'},
    {'http':'121.31.195.154'},
    {'http': '61.135.217.7'},
    {'https': '175.8.26.216'},
    {'http': '106.75.9.39'},
    {'http': '219.141.153.41'},
]

for i in range(5):
    proxy = random.choice(proxies)
    proxy_handler= urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)

    url = 'https://blog.csdn.net/xiaohuoche175/article/details/81299303'

    try:
        response = opener.open(url,timeout=5)
        if response.code != 200:
            proxies.remove(proxy)
    except Exception as e :
        pass
    print(proxy)