import urllib
from urllib import request,parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def getPythonJob():
    url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'

    data = {
        "pageSize": "10",
        "t": "0.661976834936195",
        "keyWord": "python",
        "pageIndex": "1",
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data=data,headers=headers)
    response = urllib.request.urlopen(req)

    response = response.read().decode('utf-8')
    print(response)
    response = json.loads(response)

    returnValue = response['returnValue']['datas']
    print(returnValue)
    for job in returnValue:
        #获取部门departmentName
        departmentName = job['departmentName']
        #获取要求
        requirement = job['requirement']

        print(departmentName,requirement)

def getAllJob(url):

    data = {
        "pageSize": "10",
        "t": "0.661976834936195",
        "pageIndex": "1",
    }
    #获取全部岗位数量页数
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,headers)
    response = urllib.request.urlopen(req).read()
    data = json.loads(response)
    totalPage = data['returnValue']['totalPage']

    for p in range(1,int(totalPage) + 1):
        data = {
        "pageSize": "10",
        "t": "0.661976834936195",
        "pageIndex": str(p),
        }

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data=data,headers=headers)
    print(req)
    response = urllib.request.urlopen(req).read()
    print(response)
    returnValue = json.loads(response)['returnValue']['datas']
    print(returnValue)

    for job in returnValue:
        #获取部门departmentName
        departmentName = job['departmentName']
        #获取要求
        requirement = job['requirement']

        print(departmentName,requirement)

if __name__ == '__main__':
    starturl = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
    getAllJob(starturl)
    # getPythonJob()
