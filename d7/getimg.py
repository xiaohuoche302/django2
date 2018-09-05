# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/20 9:10
@Author  : Fate
@File    : house.py
'''

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
    获取房子信息
    :param url: 页数url
    :return:
    '''
    # url = "https://gz.lianjia.com/ershoufang/pg1/"

    response = requests.get(url, headers=headers)
    # print(response.text)


    mytree = lxml.etree.HTML(response.text)


    oneImg = mytree.xpath('/html/body/div[4]/div[1]/ul/li[1]/a/img/@data-original')[0]
    return oneImg

if __name__ == '__main__':

    url = "https://gz.lianjia.com/ershoufang/pg1/"
    oneimg = getHouseInfo(url)
    r = requests.get(oneimg)
    r.raise_for_status()
    with open('test.jpg', 'wb') as f:
        f.write(r.content)

