import os

import requests
import lxml
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

url = 'http://v.qq.com/detail/7/79890.html'

response = requests.get(url,headers=headers).content.decode('gbk',errors='ignore')

mytree = lxml.etree.HTML(response)

jobList = mytree.xpath('/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/span/div/div/div[2]/div/ul')
for job in jobList:
    for i in range(0,5):
        joburl = job.xpath('./li/a/@href')[i]
        print(joburl)

cmd = 'you-get http://v.qq.com/x/cover/gmc3zyqu15w9fgu.html?vid=p00272p6afh'
os.system(cmd)


