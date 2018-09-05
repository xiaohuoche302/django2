import urllib
from urllib import request,parse
import re

# https://sou.zhaopin.com/jobs/searchresult.ashx?jl=广州&kw=python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def getJobBum(jl,kw):
    '''
    获取岗位数量
    :param jl:地区
    :param kw:关键字
    :return:岗位数量
    '''
    search = {'jl':jl,'kw':kw}
    search = urllib.parse.urlencode(search)
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + search

    req = urllib.request.Request(url,headers=headers)

    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    '''
    <em>1719</em>
    '''
    jobre = '<font color="red">(\d+)</font>'
    jobnum = re.findall(jobre,html)[0]
    print(html,jobnum)


if __name__ == '__main__':
    getJobBum(jl='广州',kw='python')