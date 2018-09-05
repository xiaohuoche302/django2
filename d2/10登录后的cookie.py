import urllib
from  urllib import request

headers = {
    'Cookie':'uuid_tt_dd=10_19001789880-1522758625602-866809; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; kd_user_id=2ca48ca1-63b3-4857-be96-9b7d2d241e80; UN=xiaohuoche175; smidV2=201806281434570a5209bd65d7d917e2089d1aff56102200ce8761cff27a460; __utma=17226283.1466348918.1529930859.1529930859.1531126856.2; __utmz=17226283.1531126856.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; UM_distinctid=164ee41c57511a-09a14f3bd1067c-5e442e19-100200-164ee41c5772c1; dc_session_id=10_1534143979743.482919; ViewMode=contents; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1534213588,1534227314,1534235122,1534251654; UserName=xiaohuoche175; UserInfo=e6ZpBCAW72xBYqQqTY2shzW8SpkTIQuYII31h%2Bj6Uii%2BUuipaU0BE6yrwRDtlk%2FwF9FSz71hKRhqLC%2FGcoKO3xl%2F9%2BDnxb0GEUeT%2FWYcjOHjGnRA0QoCwsrjSviqD83bVBzKg3lYZg28eQqWj0azwg%3D%3D; UserNick=Bruce%E6%9D%8E; AU=0A1; BT=1534251728194; UserToken=e6ZpBCAW72xBYqQqTY2shzW8SpkTIQuYII31h%2Bj6Uii%2BUuipaU0BE6yrwRDtlk%2FwF9FSz71hKRhqLC%2FGcoKO3xl%2F9%2BDnxb0GEUeT%2FWYcjOHjGnRA0QoCwsrjSviqD83bUB8syRpNMBkJeKLNzIG1q2REAIcGSHUk8TlmveRFmfVticiRlw5pj23DgUJqOYv8; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1534251668; dc_tos=pdgdd5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

url = 'https://blog.csdn.net/xiaohuoche175'

req = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
