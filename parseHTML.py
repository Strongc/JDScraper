# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function,unicode_literals


#----------module import---------

import time
import codecs

from bs4 import BeautifulSoup

from writeData import jdWriteData

#----------module import----------


#----------function definition----------

def parsePageHTML(html,fileName):
    'Parse the HTML'
    
    if html == None:
        return None

    # parse the HTML
    try:
        soup = BeautifulSoup(html,'html.parser')
        div_J_searchWrap = soup.body.find('div',attrs={'id':'J_searchWrap'})
        div_m_list = div_J_searchWrap.find('div',attrs={'class':'m-list'})
        div_ml_wrap = div_m_list.find('div',attrs={'class':'ml-wrap'})
        div_J_goodsList = div_ml_wrap.find('div',attrs={'id':'J_goodsList'})
        ul = div_J_goodsList.ul
        parsePageHTML2(ul,fileName)
    except Exception:
        print('parse error:',fileName.encode('utf-8'))
        return None  


def parsePageHTML2(ul,fileName):
    'Parse the data from HTML'
    
    if ul == None:
        return None
        
    try:
        ul = BeautifulSoup(ul,'html.parser')
    except:
        pass 
            
    # parse the data
    __i__ = 1
    products = ul.find_all('li')
    for product in products:

        items = product.find_all('div',attrs={'class':'tab-content-item'})
        if items:
            for item in items:
                indicator = jdWriteData(item,fileName)
                if indicator == 0:
                    __i__ = 0  
        else:
            indicator = jdWriteData(product,fileName)
            if indicator == 0:
                __i__ = 0
         
    # print write error
    if __i__ == 0:        
        print('write error:',fileName.encode('utf-8'))
        
#----------function definition----------


#----------unit test----------

if __name__ == '__main__':
    begin = time.time()

    fileName = u'JDData_2016-04-21/jdPrice_2016-04-21_酱油_&cid2=1584&cid3=2677&ev=_1'
    
    html = codecs.open('unitTest_html')
    html2 = codecs.open('unitTest_html2')
    parsePageHTML(html,fileName)
    parsePageHTML2(html2,fileName)

    end = time.time()
    print('time:',end-begin)
#----------unit test----------