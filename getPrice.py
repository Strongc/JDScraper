# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


import time
import random

import requests

from scraperHeaders import USER_AGENT_LIST,PROXIES


def getPrice(goodsID):
    if goodsID==None:
        return None
    
    # request head
    userAgent = random.choice(USER_AGENT_LIST)
    proxies = random.choice(PROXIES)
    headers = {
'Accept':'*/*',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'p.3.cn',
'Referer':'http://search.jd.com/',
'user-agent':userAgent,
'http':proxies,
    }
    
    url = ''.join(['http://p.3.cn/prices/mgets?&skuIds=',goodsID])
    r = requests.get(url,headers)
    jsonData = r.json()
    
    price = jsonData[0]['p']
    return price
    
    
if __name__ == '__main__':
    begin = time.time()
    
    price = getPrice('J_2111167')
    print(price)
    
    end = time.time()
    
    print('time:',end-begin)