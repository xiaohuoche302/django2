import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

def getFm(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode('utf-8')

    mytree = lxml.etree.HTML(html)

    fmList = mytree.xpath('//ul[@class="m-cvrlst f-cb"]/li')


    for fm in fmList:
        fmName = fm.xpath('./div[@class="u-cover u-cover-1"/p/a/@title]')[0]
        fmUrl = 'https://music.163.com' + fm.xpath('./div[@class="u-cover u-cover-1"/a/@href]')[0]
        print(fmName,fmUrl)

    # return fmUrl

def getPage(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode('utf-8')

    mytree = lxml.etree.HTML(html)

    pageNum = mytree.xpath('//*[@id="m-pl-pager"]/div/a[10]/text()')[0]

    return pageNum

def getmsg(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode('utf-8')

    mytree = lxml.etree.HTML(html)

    #页数
    # pageNum = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[2]/div[2]/div/nav/ul/li[6]/a/span/text()')[0]

    #书名
    bookname = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[1]/div[2]/div[2]/h1/text()')[0]

    #简介
    bookjj = mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[1]/div[3]/article/p/text()') or mytree.xpath('//*[@id="root"]/main/section/div/div[2]/div[1]/div[1]/div[3]/article/p/span/text()')

    # print(bookname,",".join(bookjj))
    #章回
    zhList = mytree.xpath('//div[@class="dOi2 sound-list-wrapper"]/div[2]/ul/li/div[2]/a')
    for zh in zhList:
        zhanghui = zh.xpath('./text()')[0]
        zhanghuifm = 'https://www.ximalaya.com' + zh.xpath('./@href')[0]
    # zhDict[zhanghui] = zhanghuifm
    # print(zhDict)
    #     print(zhanghui,zhanghuifm)
def msgpage(url):
    response = requests.get(url,headers=headers)
    html = response.content.decode('utf-8')

    mytree = lxml.etree.HTML(html)
    msgPage = mytree.xpath('//ul[@class="Yetd pagination-page"]//li[last()-1]/a/span/text()')[0]
    # print(msgPage)
    return msgPage





if __name__ == '__main__':
    # starturl = 'https://music.163.com/discover/playlist'
    # for i in range(1,int(getPage(starturl)) + 1):
    #     url = 'https://www.ximalaya.com/youshengshu/wenxue/p%d' % i * 35
    #     newurl = getFm(url)
    #     for i in range(1,int(msgpage(newurl)) + 1):
    #         nnewurl = newurl + 'p%d' % i
    #         print(nnewurl)
    # starturl = 'https://music.163.com/discover/playlist'
    # print(getPage(starturl))
    url = 'https://music.163.com/discover/playlist'
    getFm(url)