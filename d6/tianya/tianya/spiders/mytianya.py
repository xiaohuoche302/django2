# -*- coding: utf-8 -*-
import re
from tianya.items import TianyaItem
import scrapy

class MytianyaSpider(scrapy.Spider):
    name = 'mytianya'
    allowed_domains = ['bbs.tianya.cn']
    start_urls = ['http://bbs.tianya.cn/post-140-393968-1.shtml']

    def parse(self, response):
        #z邮箱正则
        emailRe = "[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,4}"
        print(response.text)
        html = response.body.decode('utf-8')

        emailList = re.findall(emailRe,html,re.I)
        print(emailList)

        item = TianyaItem()
        item["email"] = emailList

        #返回你的存储对象
        for e in emailList:
            item["email"] = e.strip()
            yield item


