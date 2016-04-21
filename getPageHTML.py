# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#---------module import---------

import random
import time
import codecs

import requests

from scraperHeaders import USER_AGENT_LIST,PROXIES

#----------module import----------


#----------function definition----------

def getPageHTML(categoryName,pageURL):
    'Request for the HTML of a certain page'
    
    # request head
    userAgent = random.choice(USER_AGENT_LIST)
    proxies = random.choice(PROXIES)
    headers = {
'Accept':'text/html',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'search.jd.com',
'Referer':'http://www.jd.com/',
'user-agent':userAgent,
'http':proxies,
    }
    
    # request for the HTML
    try:
        r = requests.get(pageURL,headers)
    except (requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        print('connect error:',(categoryName).encode('utf-8'))
        return None
    return r.content

#-----------function definition----------


#----------unit test----------

if __name__ == '__main__':
    
    begin = time.time()
    
    categoryName = u'酱油'
    pageURL = u'http://search.jd.com/search?enc=utf-8&psort=3&page=1&s=1&keyword=酱油&cid2=1584&cid3=2677&ev='
    pageURL2 = u'http://search.jd.com/s_new.php?enc=utf-8psort=3&scrolling=y&page=2&s=31&keyword=酱油&cid2=1584&cid3=2677&ev=' 
    #html = getPageHTML(categoryName, pageURL) 
    html2 = getPageHTML(categoryName, pageURL2) 
    
    #with codecs.open('unitTest_html','wb') as f:
    #    f.write(html)
    with codecs.open('unitTest_html2','wb') as f:
        f.write(html2)    
    
    end = time.time()
    print('time:',end-begin)
    
#----------unit test----------