import requests
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"
response = requests.get(url, headers=headers)
html = response.content.decode('utf-8')
msgList = json.loads(html)['returnValue']
# print(msgList)
page=msgList['pageSize']
print(page)