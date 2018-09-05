import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getHTML(url):

    '''
    获取网页源码
    :param url:
    :return:HTML源码
    '''
    response = requests.get(url,headers=headers)
    return response.content.decode('utf-8','ignore')

def getUrl(url):
    '''
    筛选出url
    :param url: 上一层级的url
    :return:
    '''
    html = getHTML(url)
    urlre = '<a .*href=\"(https?://.*?)\" .*>'

    #预编译
    urlc = re.compile(urlre)

    urlList = urlc.findall(html)

    return urlList

def deepSpider(url,depth):
    '''
    深度爬虫
    :param url:起始url
    :param depth: 深度
    :return:
    '''
    print('\t\t\t' * depthDict[url],"第%d层级数据：%s" % (depthDict[url],url))

    #超出层级退出
    if depthDict[url] >= depth:
        return

    #生成新的url
    sonUrlList = getUrl(url)
    # print(sonUrlList)
    for newUrl in sonUrlList:
        #去重
        if newUrl not in depthDict:
            depthDict[newUrl] = depthDict[url] + 1
            deepSpider(newUrl,depth)

if __name__ == '__main__':
    #起始url
    starturl = "https://www.baidu.com/s?wd=富二代"

    #层级控制{"url","层级"}
    depthDict = {}
    depthDict[starturl] = 1

    deepSpider(starturl,4)