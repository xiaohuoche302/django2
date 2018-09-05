import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
url = 'https://jobs.51job.com/guangzhou/p2/'

def getJob(url):
    response = requests.get(url,headers=headers).content.decode('gbk')
    mytree = lxml.etree.HTML(response)

    jobList = mytree.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div')
    print(jobList)
    for job in jobList:
        #抓取公司名字：/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[1]/span[1]/a

        jobName = job.xpath('.//p[@class="info"]/span/a/@title')[0]
        jobName = job.xpath('./p[1]/span[1]/a/@title')[0]
        jobName = job.xpath('./p[1]/span[1]/a/text()')[0].strip()

        # 抓取公司网址：/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[1]/span[1]/a
        jobUrl = job.xpath('./p[1]/span[1]/a/@href')[0]

        # 抓取公司地址:/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[1]/a
        jobAddress = job.xpath('./p[1]/a/@title')[0]

        #所在城市：/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[1]/span[2]
        jobCity = job.xpath('./p[1]/span[2]/text()')[0]

        #工作需求：/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[2]
        jobOrder = job.xpath('./p[2]/text()')[0].strip()+','+job.xpath('p[2]/text()')[1].strip()+','+job.xpath('p[2]/text()')[2].strip()+','+job.xpath('p[2]/text()')[3].strip()

        #公司简介:/html/body/div[3]/div[3]/div[1]/div[2]/div[1]/p[3]
        jobintro = job.xpath('./p[3]/@title')[0]
        print(jobName,jobUrl,jobAddress,jobCity,jobOrder,jobintro)
              # jobUrl,jobAddress)

getJob(url)