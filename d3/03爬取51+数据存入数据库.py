import urllib
from urllib import request,parse
import json
import requests
from bs4 import BeautifulSoup
import pymysql

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html'

response = requests.get(url,headers=headers).content.decode('gbk')

soup = BeautifulSoup(response,'lxml')
jobList = soup.select('#resultList > div.el')
# print(response)

for job in jobList[1:]:
    #职位名
    # resultList > div:nth-child(4) > p > span > a
    jobname = job.select('p > span > a')[0]['title']

    #职位详情网址
    # resultList > div:nth-child(4) > p > span > a
    joburl = job.select('p > span > a')[0]['href']

    #公司名
    # resultList > div:nth-child(4) > span.t2 > a
    jobIofo = job.select('span.t2')[0].text

    #工作地点
    # resultList > div:nth-child(4) > span.t3
    jobcompany = job.select('span.t3')[0].text

    #薪资
    # resultList > div:nth-child(4) > span.t4
    jobmoney = job.select('span.t4')[0].text

    #发布时间
    # resultList > div:nth-child(4) > span.t5
    jobtime = job.select('span.t5')[0].text

    print(jobname,joburl,jobIofo,jobcompany,jobmoney,jobtime)

    #写入文本
    with open('tencent.txt','a+',encoding='utf-8',errors='ignore') as f:
        f.write(str((jobname,joburl,jobIofo,jobcompany,jobmoney,jobtime))+ '\n')
        f.flush()

#数据库信息

conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',
                       database='world',port=3306,charset='utf8')

#游标
cur = conn.cursor()

#读取
with open('tencent.txt','r',errors='ignore',encoding='utf-8') as f :
    jobList = f.readlines()
    for job in jobList:
        job = eval(job)
        sql = "INSERT INTO tencent(jobname,joburl,jobIofo,jobcompany,jobmoney,jobtime)VALUES " \
              "(%r,%r,%r,%r,%r,%r)" % (job[0], job[1], job[2], job[3], job[4], job[5])
        print(job)
        print(sql)
        cur.execute(sql)
        conn.commit()
cur.close()
conn.close()