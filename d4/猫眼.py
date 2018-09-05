import requests
import json
import math

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

def getMovieJson(url):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        html = response.text
        return html
    else:
        return None

def parse_one_page(html):
    if html:
        data = json.loads(html)['cmts']
        for item in data:
            yield {
                'nickName': item['nickName'],
                'cityName': item['cityName'],
                'content': item['content'].strip().replace('\n', ''),
                'score': item['score'],
                'startTime': item['startTime']
            }

def save_to_text(url):
    html = getMovieJson(url)
    with open('一出好戏.txt','a+',encoding='utf-8',errors='ignore') as f:
        for item in parse_one_page(html):
            f.write(str(item['startTime'] + "," + item['nickName']
                        + "," + item['cityName'] + "," + str(item['score']) + "," + item['content']
                        + '\n'))

if __name__ == '__main__':
    pageNum = math.ceil(74085/15)
    for i in range(1,pageNum):
        url = "http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=%d" % i
        save_to_text(url)