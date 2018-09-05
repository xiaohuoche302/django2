#get传参
import urllib.request
import urllib.parse
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def getWD(wd):
    #url 编码
    wd = urllib.parse.urlencode({"wd":wd})
    print(wd)
    url = 'https://www.baidu.com/s?' + wd
    #url 解码
    print(urllib.parse.unquote(wd))
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))
    print(response.url)

if __name__ == '__main__':
    wd = input("请输入要查找的关键字：")
    getWD(wd)