# -*- coding: utf-8 -*-
import scrapy


class MyweixinSpider(scrapy.Spider):
    name = 'myweixin'
    allowed_domains = ['weixin.sogou.com/']
    start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    def parse(self, response):
        # print(response.text)

        publicNumList = response.xpath('//div[@class="txt-box"]')
        for wx in publicNumList:
            # 微信公众号url
            wechatPublicNumurl = wx.xpath('.//div[@class="s-p"]/a/@href').extract()[0]