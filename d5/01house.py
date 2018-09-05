import requests
import lxml
from lxml import etree
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

def getHouseInfo(url):
    '''
    获取房源信息
    :param url: 页数url
    :return:
    '''
    # url = "https://gz.lianjia.com/ershoufang/pg1/"
    response = requests.get(url,headers=headers)

    mytree = lxml.etree.HTML(response.text)

    #房子列表
    houseList = mytree.xpath('/html/body/div[4]/div[1]/ul/li')
    # print(houseList)
    for house in houseList:
        #图片
        houseImg = house.xpath('./a/img/@data-original')[0]

        # 标题
        houseAlt = house.xpath('./div[@class="info clear"]/div/a/text()')[0]

        # 位置
        houseAddress = house.xpath('.//div[@class="houseInfo"]/a/text()')[0] + house.xpath('.//div[@class="houseInfo"]/text()')[0]

        # 楼层 小区
        positionInfo = house.xpath('.//div[@class="positionInfo"]/text()')[0] + house.xpath('.//div[@class="positionInfo"]/a/text()')[0]

        # 总价
        totalPrice = house.xpath('.//div[@class="totalPrice"]/span/text()')[0] + "万"

        # 单价
        unitPrice = house.xpath('.//div[@class="unitPrice"]/span/text()')[0]
        biaoqian = house.xpath('.//span[@class="taxfree"]/text()') + house.xpath('.//span[@class="haskey"]/text()') + house.xpath('.//span[@class="subway"]/text()')
        # print(biaoqian)
        biaopian = (' '.join(biaoqian))
        print(biaopian)




if __name__ == '__main__':
    url = "https://gz.lianjia.com/ershoufang/pg1/"
    getHouseInfo(url)





