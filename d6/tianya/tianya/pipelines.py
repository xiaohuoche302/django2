# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianyaPipeline(object):
    def __init__(self):
        pass

    def open_spider(self,spider):
        '''
        爬虫开启的时候调用一次
        :param spider:
        :return:
        '''
        self.f = open('tianya.txt','w',encoding='utf-8',errors='ignore')

    #持久化
    def process_item(self, item, spider):
        '''
        写入txt
        :param item: 存储对象
        :param spider: 爬虫名
        :return:
        '''

        self.f.write(item['email'] + '\n')
        return item

    def close_spider(self,spider):
        '''
        爬虫关闭的时候一次
        :param spider:
        :return:
        '''

        self.f.close()

    def __del__(self):
        pass