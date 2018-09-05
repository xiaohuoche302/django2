import requests
import lxml
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
#获取想要抓取的url


#获取岗位信息
def getjob(url):
    response = requests.get(url,headers=headers).content.decode('utf-8')
    # print(response)
    mytree = lxml.etree.HTML(response)
    # print(mytree)


    jobList = mytree.xpath('//*[@id="comments"]/div[@class="comment-item"]')
    # print(jobList)
    for job in jobList:
        jobName = job.xpath('./div[1]/a/@title')[0]
        jobcomment = job.xpath('./div[2]/p/span/text()')[0]

        print(jobName,jobcomment)
        yield {
            "jobName":jobName,
            "jobcomment":jobcomment
        }

if __name__ == '__main__':
    for i in range(0,11):
        url = 'https://movie.douban.com/subject/30122633/comments?start=%d' % (i*20)

        with open('豆瓣.txt', 'a+',encoding='utf-8') as f :
            for data in getjob(url):
                f.write(str((data['jobName'], data['jobcomment'] + '\n')))