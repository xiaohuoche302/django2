import urllib
from urllib import request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

i = 0
while True:
    url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d' %( i * 20 )
    i += 1

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    if response.code == 200:
        response = response.read().decode('utf-8')
        data = json.loads(response)['data']
        print(data)
        for movie in data:
            directors = movie['directors']
            rate = movie['rate']
            print(directors,rate)
    else:
        print(i)
        break